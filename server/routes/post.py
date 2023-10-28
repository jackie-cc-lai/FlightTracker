def postViews(app):
    @app.route('/auth', method=['POST'])
    def auth():
        return "Authorizing"