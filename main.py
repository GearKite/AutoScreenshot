import os
from flask import Flask, send_file, request, Response, abort
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)


@app.route("/")
def screen():
    if request.args.get("secret") != os.environ.get("SHARED_SECRET"):
        abort(400)

    os.system("spectacle --background --output screen.png --nonotify --fullscreen")

    return send_file("screen.png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088, debug=False)
