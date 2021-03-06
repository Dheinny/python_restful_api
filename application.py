# _*_ coding: utf-8 _*_

from os import getenv
from dotenv import load_dotenv
load_dotenv()

from apps import create_app

app = create_app(getenv("FLASK_ENV") or "default")

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = app.config["APP_PORT"]
    debug = app.config["DEBUG"]

    #run Flask web server
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )


