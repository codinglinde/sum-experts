from flask import Flask, jsonify, request
from db_utils import get_all_advisors, get_all_bookings, get_all_customers, get_all_advisors_by_specialism, get_all_booking_availability_by_date_and_specialism, add_booking


app = Flask(__name__)


@app.route('/advisors')
def get_advisors():
    result = get_all_advisors()
    return jsonify(result)

@app.route('/advisors/<spec>')
def get_advisors_by_specialism(spec):
    result = get_all_advisors_by_specialism(spec)
    return jsonify(result)

@app.route('/booking')
def get_bookings():
    result = get_all_bookings()
    return jsonify(result)

@app.route('/booking', methods=['PUT'])
def book_appt():
    booking = request.get_json()
    add_booking(
        _date=booking['_date'],
        advisor=booking['advisor'],
        time=booking['time'],
        customer=booking['customer']
    )

    return booking

@app.route('/customers')
def get_customers():
    result = get_all_customers()
    return jsonify(result)


@app.route('/availability/<date>/<specialism>')
def get_availability(date, specialism):
    res = get_all_booking_availability_by_date_and_specialism(date, specialism)
    return jsonify(res)



if __name__ == '__main__':
    app.run(debug=True, port=5000)