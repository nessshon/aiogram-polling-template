import asyncio
import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from .bot import middlewares, routes, commands
from .config import Config, load_config
from .db.database import Database


async def on_shutdown(dispatcher: Dispatcher, bot: Bot) -> None:
    """
    Shutdown event handler. This runs when the bot shuts down.
    """
    db: Database = dispatcher.get("db")
    config: Config = dispatcher.get("config")
    await bot.send_message(chat_id=config.bot.DEV_ID, text="#BotStopped")
    await commands.delete(bot)
    await bot.delete_webhook()
    await bot.session.close()
    await db.close()


async def on_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    """
    Startup event handler. This runs when the bot starts up.
    """
    config: Config = dispatcher.get("config")
    await bot.send_message(chat_id=config.bot.DEV_ID, text="#BotStarted")


async def main() -> None:
    """
    Main function that initializes the bot and starts the event loop.
    """
    config = load_config()
    db = Database(config.database)
    storage = RedisStorage.from_url(
        url=config.redis.dsn(),
        connection_kwargs={"decode_responses": True}
    )
    bot = Bot(
        token=config.bot.TOKEN,
        parse_mode=ParseMode.HTML,
    )
    dp = Dispatcher(
        storage=storage,
        config=config,
        bot=bot,
        db=db,
    )

    # Register startup handler
    dp.startup.register(on_startup)
    # Register shutdown handler
    dp.shutdown.register(on_shutdown)
    # Register middlewares
    middlewares.register(dp, config=config, session=db.session)
    # Include routes
    routes.include(dp)

    # Initialize database
    await db.init()
    # Initialize commands
    await commands.setup(bot)
    # Start the bot
    await bot.delete_webhook()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # noqa
        handlers=[
            TimedRotatingFileHandler(
                filename=f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",
                when="midnight",
                interval=1,
                backupCount=1,
            ),
            logging.StreamHandler(),
        ],
    )
    # Set logging level for aiogram to CRITICAL
    aiogram_logger = logging.getLogger("aiogram.event")
    aiogram_logger.setLevel(logging.CRITICAL)
    # Run the bot
    asyncio.run(main())
