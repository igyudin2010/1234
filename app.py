from webob import Request, Response

from api import API


app = API()


@app.route("/players")
class PlayerView:
    def get(self, request, response, **kwargs):
        pass


@app.route("/home")
def home(request, response):
    response.text = "Hello from home page!"