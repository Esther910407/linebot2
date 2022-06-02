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

line_bot_api = LineBotApi('g2ZhzWz4O7D3UP38nrSAntthSl7vM8kRiyoqzD3D0KtvkDvKjVITOlZAPkMsphSeCHvC+6LgGN7flqTSfwiVKkS+jUOhaP4s8lSVNtBTf0GlRhKBfq9OjuoD/xY/dfx2MZkLIV5htASe5IdtrVW3lgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d44f034eb368836bdbf9c417206e760c')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎'))


if __name__ == "__main__":
    app.run()