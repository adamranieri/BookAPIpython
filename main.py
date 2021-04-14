import logging

from flask import Flask
from routes import book_routes

app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
book_routes.create_routes(app)


if __name__ == '__main__':
   app.run()
