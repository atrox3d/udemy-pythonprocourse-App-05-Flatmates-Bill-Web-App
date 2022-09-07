from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

from flatmates_bill import flat                             # add flatmatesbill's class to the broject

app = Flask(__name__)                                       # initialize app


class HomePage(MethodView):                                 # logic of the homepage

    def get(self):                                          # http get request
        return render_template('index.html')                # render templates/index.html


class BillFormPage(MethodView):                             # logic of the bill form page

    def get(self):                                          # http get request
        return render_template('bill_form_page.html',       # render templates/bill_form_page.html
                               billform=BillForm())         # form object


class ResultsPage(MethodView):                              # logic of the results page

    def post(self):                                         # http post request
        billform = BillForm(request.form)                   # get form data from request
        amount = billform.amount.data                       # get amount field value from processed form
        period = billform.period.data                       # get period field value from processed form

        name1 = billform.name1.data                         # get name1 field value from processed form
        days_in_house1 = billform.days_in_house1.data       # get days_in_house field value from processed form

        name2 = billform.name2.data                         # get name1 field value from processed form
        days_in_house2 = billform.days_in_house2.data       # get days_in_house field value from processed form

        the_bill = flat.Bill(float(amount), period)         # instantiate Bill
        flatmate1 = flat.Flatmate(name1,
                                  float(days_in_house1))    # instantiate Flatmate 1
        flatmate2 = flat.Flatmate(name2,
                                  float(days_in_house2))    # instantiate Flatmate 2

        return render_template(
            'results.html',
            name1=name1,
            amount1=flatmate1.pays(the_bill, flatmate2),
            name2=name2,
            amount2=flatmate1.pays(the_bill, flatmate1),
        )


class BillForm(Form):                                       # fields of the bill form
    amount = StringField("Bill amount: ", default="100")
    period = StringField("Bill period: ", default="August 2022")

    name1 = StringField("Name: ", default="Fab")
    days_in_house1 = StringField("Days in the house: ", default=31)

    name2 = StringField("Name: ", default="Rob")
    days_in_house2 = StringField("Days in the house: ", default="15")

    button = SubmitField("Calculate")


app.add_url_rule(                                           # adds a route
    '/',                                                    # url path
    view_func=HomePage.as_view('home_page')                 # logic class and internal name
)
app.add_url_rule(
    '/bill',
    view_func=BillFormPage.as_view('bill_form_page')
)
app.add_url_rule(
    '/results',
    view_func=ResultsPage.as_view('results_page')
)

app.run(                                                    # run server
    debug=True                                              # enable debug, load changes
    #, host='0.0.0.0'                                       # enable external connections
)

