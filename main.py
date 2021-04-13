from flask import Flask
from routes import book_routes

app = Flask(__name__)


book_routes.create_routes(app)


if __name__ == '__main__':
   app.run()
