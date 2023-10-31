from server.service.auth import login
from flask import request


def authViews(app):
    @app.route('/login', methods=['POST'])
    def auth():
        data = request.get_json()
        response = login(data)
        return "Authorizing"
