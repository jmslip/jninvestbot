from flask import Flask
from flask_restplus import Api


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='0.1-SNAPSHOT',
            title='HR Broker - Robot',
            description='Api de web scraping e cálculos para mercado financeiro',
            doc='/doc'
        )

    def run(self):
        self.app.run(
            debug=True
        )


server = Server()
