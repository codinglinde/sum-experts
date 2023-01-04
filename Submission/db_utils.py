import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_all_advisors():
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM advisor"""

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


def get_all_advisors_by_specialism(spec):
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = f"""SELECT * FROM advisor WHERE specialism='{spec}'"""

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


def get_all_bookings():
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM bookings"""

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


def get_all_customers():
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM customer"""

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


def add_customer(first_name, last_name, address, email, phone):
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = f"""
            INSERT INTO customer
            (f_name,
             l_name,
             address,
             email_address,
             phone_num)
            VALUES      
            ('{first_name}',
             '{last_name}',
             '{address}',
             '{email}',
             '{phone}');
        """

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("There has been a connection error to our server.")

    finally:
        if db_connection:
            db_connection.close()
            print("Your detail has been saved.")


def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'name': item[0] + " " + item[1],
            '09-10': 'Not Available' if item[2] else 'Available',
            '10-11': 'Not Available' if item[3] else 'Available',
            '11-12': 'Not Available' if item[4] else 'Available',
            '12-13': 'Not Available' if item[5] else 'Available',
            '13-14': 'Not Available' if item[6] else 'Available',
            '14-15': 'Not Available' if item[7] else 'Available',
            '15-16': 'Not Available' if item[8] else 'Available',
            '16-17': 'Not Available' if item[9] else 'Available'
        })
    return mapped


def get_all_booking_availability_by_date_and_specialism(_date, specialism):
    availability = []
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = f"""
            SELECT f_name, l_name, `09-10`, `10-11`, `11-12`, `12-13`, `13-14`, `14-15`, `15-16`, `16-17`
            FROM bookings AS b
            INNER JOIN advisor AS a
            ON b.advisor = a.f_name
            WHERE b.bookingDate = '{_date}' AND a.specialism = '{specialism}'
            """

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        availability = _map_values(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return availability


# EXAMPLE 1
def add_booking(_date, advisor, time, customer):
    try:
        db_name = 'software_project_practice1'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query= f"""
                UPDATE  bookings
                SET 
                    `{time}` = 1, 
                    `{time}-booking-id` = '{customer}' 
                WHERE bookingDate = '{_date}' AND advisor = '{advisor}'
            """
        cur.execute(query)
        db_connection.commit()
        cur.close()


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")