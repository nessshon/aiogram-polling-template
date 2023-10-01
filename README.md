<h1 align="center">🤖 Aiogram Bot Template</h1>

## Installation

1. Clone this [template](https://github.com/nessshon/aiogram-polling-template):

    ```bash
    git clone https://github.com/nessshon/aiogram-polling-template
    ```

2. Go to the project folder:

    ```bash
    cd aiogram-polling-template
    ```

3. Create environment variables file:

    ```bash
    cp .env.example .env
    ```

4. Configure [environment variables](#environment-variables-reference) file:

    ```bash
    nano .env
    ```

5. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

6. Run app:

    ```bash
    python -m app
    ```

### Environment variables reference

| Variable    | Type | Description                                                 | Example       |
|-------------|------|-------------------------------------------------------------|---------------|
| BOT_TOKEN   | str  | Bot token, get it from [@BotFather](https://t.me/BotFather) | 123456:qweRTY | 
| BOT_DEV_ID  | int  | User ID of the bot developer                                | 123456789     |
| REDIS_HOST  | str  | The hostname or IP address of the Redis server              | localhost     |
| REDIS_PORT  | int  | The port number on which the Redis server is running        | 6379          |
| REDIS_DB    | int  | The Redis database number                                   | 1             |
| DB_HOST     | str  | The hostname or IP address of the database server           | localhost     |
| DB_PORT     | int  | The port number on which the database server is running     | 3306          |
| DB_USERNAME | str  | The username for accessing the database                     | user          |
| DB_PASSWORD | str  | The password for accessing the database                     | password      |
| DB_DATABASE | str  | The name of the database                                    | dbname        |
