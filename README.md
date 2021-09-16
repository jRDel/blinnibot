# blinnibot
Blinnigob Mogmomo Server Bot

Steps to setup:
1. Set correct permissions using chown, chmod on bot.py or the whole directory.
2. Make a directory called /data, and:
  ```touch birthday.json```
Edit this json to contain a dictionary with one entry, like:
  ```{"test":"01/01/2000"}```
3. Make any changes to bot.py to specify like your server, like change out blinnigob with your server name
and make sure to change the channel id of wherver you want messages to send to.
4. Make sure you have a hidden .env that holds your DISCORD_TOKEN

Python Dependencies:
- Discord.py
- json
- datetime
- asyncio
- dotenv
- os
