# Telegram-chat-bot-
Chat bot on TG. Implemented with AWS serverless tech, Lambda, API gateway, DynamoDB.

# Background
* [On-Demand-Minecraft-Sever](https://github.com/MOHOAzure/On-Demand-Minecraft-Sever)

# Requirement
* On-Demand Bot which can response to users' requests at anytime
* Low cost (deploy on EC2 is not ideal)
* In future, users can interact with bot in multiple software, including TG, Discord, and FB Messanger

# Dev
* A Telegram account + bot token key
  * See: https://github.com/MOHOAzure/Telegram-chat-bot-/blob/main/official-bot-father
* AWS Lambda (Python) + API gateway
  * See: https://github.com/MOHOAzure/Telegram-chat-bot-/tree/main/scripts/AWS-Lambda
* API Gateway
  * Add a API trigger to developed Lambda
  * Leave everthing as default settings is OK
  * Webhook URL of API Gateway to TG
