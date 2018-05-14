from flask_classy import FlaskView


class LoginView(FlaskView):
    route_base = 'auth'

    def index(self):
        return 'login index'

    def post(self):
        pass
