# TG Bot Father
* Every TG bot is crafted from TG bot father (@BotFather)
* BotFather would give you a token

# Use URL to see status of bot
* Check status and messages (only when bot is not webhooked yet)
  * https://api.telegram.org/bot{TOKEN}/getUpdates
  * This one helps find ID of group, channel, DM for bot to send message
* Remove piled up messages
  * https://api.telegram.org/bot{TOKEN}/getUpdates?offset={UPDATE_ID_IN_RETURNED_MESSAGE}

# Use URL to webhook TG and API to bot
* Hook
  * https://api.telegram.org/bot{TOKEN}/setWebhook?url={API_TO_BOT}
* Delete webhook (just get rid of things behind /setWebhook)
  * https://api.telegram.org/bot{TOKEN}/setWebhook

# Ref
* Simple Telegram Bot with Python and AWS Lambda, Daniils Petrovs, https://levelup.gitconnected.com/simple-telegram-bot-with-python-and-aws-lambda-5eab1066b466
* Develop your Telegram ChatBot with AWS API Gateway, DynamoDB, and Lambda Functions, 
Rodrigo Dutcosky, https://aws.plainenglish.io/develop-your-telegram-chatbot-with-aws-api-gateway-dynamodb-lambda-functions-410dcb1fb58a
