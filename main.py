from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        return render_template('bill_form_page.html', billform=BillForm())


class ResultsPage(MethodView):
    def post(self):
        billform =BillForm(request.form)
        amount = billform.amount.data
        return amount


class BillForm(Form):
    amount = StringField("Bill amount: ")
    period = StringField("Bill period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
