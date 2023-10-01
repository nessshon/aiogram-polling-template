from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def setup(bot: Bot) -> None:
    """
    Setup bot commands.
    """
    commands = [
        BotCommand(command="start", description="Restart bot"),
    ]

    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats(),
    )


async def delete(bot: Bot) -> None:
    """
    Delete bot commands.
    """
    await bot.delete_my_commands(
        scope=BotCommandScopeAllPrivateChats(),
    )
