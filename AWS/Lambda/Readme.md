# Lambda setup

## Dependency
* OSS: [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
### Layer
* (tricky) Build lib, zip the lib, and then put dependency to layer
* In short 
  * create a dir, named 'python', for building lib and go inside
  * use virtual env and then you can easily find the installed lib in the following step and this step make your working env clean
  * install lib
  * zip the whole dir
  * use aws to put it to Lambda layer
    * `aws lambda publish-layer-version --layer-name telebot --zip-file fileb://telebot_layer.zip --compatible-runtimes python3.7`

## Environment variables
* TELEGRAM_TOKEN
  * TG bot token
* CHAT_ID_DM
  * Dev direct message to bot
* CHAT_ID_GROUP_TEST
  * Id of test group (add bot to here, before it formally join the group full of users)
* CHAT_ID_GROUP_MAIN
  * Id of mail group (a group full of users)
* DDB_NAME
  * DynamoDB records user commands
* GAME_SERVER_TRIGGER
  * The main job of the job is to turn on game server, and this is an API acts as a trigger to the server

## Permission
* Lambda basic
* DDB
  * read, write
  
