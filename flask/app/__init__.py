from flask import Flask
app = Flask(__name__)
from app.welcome.views import mod as flask_welcome_mod
