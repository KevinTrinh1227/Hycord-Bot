## 🛠 set-up

1. Create a "`.env`" file with your tokens and API keys

   ```sh
   DISCORD_BOT_TOKEN=<YOUR_DISCORD_BOT_TOKEN>
   TWITCH_CLIENT_ID=<YOUR_TWITCH_APP_CLIENT ID>
   TWITCH_CLIENT_SECRET=<YOUR_TWITCH_APP_CLIENT_SECRET>
   ```

2. Configure the config.json file appropriately

   ```sh
    {
    "bot_prefix": "<DESIRED_PREEFIX>",
    "embed_color": "<HEX_COLOR_CODE>",
    "twitch_username": "<YOUR_TWITCH_USERNAME>"
    }
   ```

3. Install the modules

   ```sh
   pip install discord.py
   ```
   ```sh
   pip install python-dotenv
   ```
   ```sh
   pip install requests
   ```

## 🚀 activate bot in terminal

1. build and run Discord bot

   ```sh
   python main.py
   ```