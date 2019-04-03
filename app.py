from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('oLfxR/ZpZOUmXipkU8OqHkGE9AR0xGJuFqrzl/zhf8mKFGyg0ArOhHS24BeEfcYGpmCSwzsHTyVWFxqKV+dCDsdxdo+OsKr+EzbbYAkHqY8KDORIFiFigOvt+U2+ex0kH4ahb1uqYoWZZk9Qk2u1rwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('16b4f1fd0118a67246578eecf223af93')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '無法辨別訊息'

    if msg == 'hi':
    	r = 'hi'
    elif msg == '你吃飯了嗎?':
    	r = '還沒'
    	
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=))


if __name__ == "__main__":
    app.run()