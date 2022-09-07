from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

app = Flask(__name__)                                   # initialize app


class HomePage(MethodView):                             # logic of the homepage

    def get(self):                                      # http get request
        return render_template('index.html')            # render templates/index.html


class BillFormPage(MethodView):                         # logic of the bill form page

    def get(self):                                      # http get request
        return render_template('bill_form_page.html',   # render templates/bill_form_page.html
                               billform=BillForm())     # form object


class ResultsPage(MethodView):                          # logic of the results page

    def post(self):                                     # http post request
        billform = BillForm(request.form)               # get form data from request
        amount = billform.amount.data                   # get amount value from processed form
        return amount


class BillForm(Form):                                   # fields of the bill form
    amount = StringField("Bill amount: ")
    period = StringField("Bill period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


app.add_url_rule(                                       # adds a route
    '/',                                                # url path
    view_func=HomePage.as_view('home_page')             # logic class and internal name
)
app.add_url_rule(
    '/bill',
    view_func=BillFormPage.as_view('bill_form_page')
)
app.add_url_rule(
    '/results',
    view_func=ResultsPage.as_view('results_page')
)

app.run(                                                # run server
    debug=True                                          # enable debug, load changes
    #, host='0.0.0.0'                                   # enable external connections
)

