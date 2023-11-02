def postViews(app):
    @app.route('/save', method=['POST'])
    def save_flight():
        return "Authorizing"
