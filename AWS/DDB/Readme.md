# DynamoDB Setup
  
| Field Name    | Type          | Note |
| ------------- | ------------- | ------------- |
| datetime      | string        | Partition key; The time when a message is sent to the bot |
| sender_id     | string        | Sort key; The ID of Telegram user who sends the message |
| chat_id       | string        | The ID of Telegram chatroom (channel) where the message is sent |
| input_text    | string        | Message content |
| sender_name   | string        | The user name of Telegram user who sends the message |
