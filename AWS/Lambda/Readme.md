# Lambda setup

## Dependency
* OSS: [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
### Layer
* To use 3rd-party lib in lambda, you need to Build lib in Amazon machine env, Zip the lib with the env, and then put zipped files to Lambda as a layer
  * [AWS official description](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
  * [Practice steps shown on this StackOverflow post](https://stackoverflow.com/questions/57688731/unable-to-import-module-lambda-function-no-module-named-pandas)
* In short 
  * create a dir, named 'python', for building lib and go inside
  * active virtual env
  * install lib
  * zip the whole dir, the virtual env 'should' be included
  * put it to Lambda layer (with aws CLI)
    * `aws lambda publish-layer-version --layer-name telebot --zip-file fileb://telebot_layer.zip`


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
  
