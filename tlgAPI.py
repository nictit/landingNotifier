import flask
import os
import threading

app = flask.Flask(__name__)

@app.route("/<reg>")
def index(reg):
    print(reg)

def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

main()
# bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt, 'rb'))