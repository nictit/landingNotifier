import flask
import os
import main

app = flask.Flask(__name__)

@app.route("/<reg>")
def index(reg):
    main.msgRecieved(str(reg))
    print(reg)

def mainn():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt, 'rb'))