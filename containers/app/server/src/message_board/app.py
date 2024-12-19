# server/src/message_board/app.py
import os
from .utils.app_utils import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
