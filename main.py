from flask.views import MethodView
from wtforms import Form
from flask import Flask

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return "Hello"


class BillFormPage(MethodView):
    def get(self):
        return "I am the bill form page"


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

app.run()
