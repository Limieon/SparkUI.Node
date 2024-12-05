import os

from dotenv import load_dotenv

load_dotenv()

SPARKUI_NODE_HOST = os.environ["SPARKUI_NODE_HOST"]
SPARKUI_NODE_PORT = int(os.environ["SPARKUI_NODE_PORT"])
SPARKUI_NODE_SECRET_KEY = os.environ["SPARKUI_NODE_SECRET_KEY"]
