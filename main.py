from flask import Flask, request, jsonify, session
from flask_restx import Api, Resource,fields


app = Flask(__name__)


api = Api(app, version="1.0",title="Agendas Api", description="An API to manage agendas ")




if __name__ == '__main__':
    app.run()
