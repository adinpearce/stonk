from flask import Flask, request, abort
import t1
import central_distributer_ver02 as cd
import certification_system as cs

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('eWn672yCwHu5eG+zXv5nfDZuVOs5etq/etG9YurCOJq0OdDNktCLSPxfLeoWmIrsJ3q2uCd25KTURwAG2fxn4fPC2j+E4kP+Mw2fFnedtSDj1J1LB+t12Yq0sRWH3LwJHmCEloAGVaKat9/KGvCQ/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8df6ddf2cfedbd154a08d606812fa885')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

def extra_message_pusher(userID, message):
    line_bot_api.push_message(
            userID, [
                TextSendMessage(text=message),
            ]
        )

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    userID = event.source.user_id
    reply_token = event.reply_token

    certificate_Status = cs.certification(userID)

    if certificate_Status == 1:
        new_message, extra_message = cd.center(message, userID, reply_token)

        reply_message = TextSendMessage(text=new_message)

        if extra_message != "":
            extra_message_pusher(userID, extra_message)
    else:
        reply_message = TextSendMessage(text="Invalid userID")

    line_bot_api.reply_message(event.reply_token, reply_message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


