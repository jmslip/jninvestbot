from flask import Flask
from flask_restplus import Api
import os


class Server:
    def __init__(self):
        self.app = Flask(__name__, instance_relative_config=True)
        self.app.config.from_pyfile('config.py')
        self.api = Api(
            self.app,
            version='0.0.2',
            title='JN Invest Bot',
            description='Api de web scraping e cálculos para mercado financeiro',
            doc='/doc'
        )

    def run(self):
        self.app.run()


server = Server()
