# How to generate bot token token
add info here on how to generate the token

# How to make it work (Development)

## Install python packages
pip install post request pandas

## Create config file with credentials
Create a config.py file on the project root and set the BOT_URL variable with the bot url with the token. 
Check the config.py.example to get an example of the needed value for BOT_URL.

## Ngrok
Download ngrok https://ngrok.com/download and place the executable file in the project root.

## Start the bot and ngrok server
- Open a terminal and from the project root path run the command `python bot.py` to start the bot.
- Open a new termianl and from the project root path run the command `./ngrok http <our_server_port>` (the default port is set to 8080)

Copy the https ngrok url that is shown in the terminal after running ngrok, and set the webhook in your browser in the following format:

`api.telegram.org/bot<your_token>/setWebHook?url=https://<your_ngrok_url.ngrok.io>/`

This response is shown when the webhook is correctly set:

`{"ok":true,"result":true,"description":"Webhook was set"}`
