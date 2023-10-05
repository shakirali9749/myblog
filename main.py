from flask import Flask, render_template, request

app = Flask(__name__)


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):
    if month:
        capitalise_month = month.capitalize()
        if capitalise_month in months:
            return capitalise_month
        return None


def valid_day(day):
    if day:
        try:
            number = int(day)
            if number > 0 and number <= 31:
                return number
            return None
        except:
            return None


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year
        return None
    else:
        return None


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')

        is_day_valid = valid_day(day)
        is_month_valid = valid_month(month)
        is_year_valid = valid_year(year)

        if not ( is_day_valid and is_month_valid and is_year_valid ):
            return render_template('index.html', error='That doesnt seem valid to me, friend!', month=month, day=day, year=year)
        else:
            return 'Thats totally a valid data'

    return render_template('index.html')
