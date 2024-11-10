from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:number>')
def prime_check(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    json_result = json.dumps(result)
    return Response(response=json_result, status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


###T2

from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

# Muista vaihtaa alla olevat tietokantayhteyden tiedot omiin arvoihisi
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="flight_game"
)

@app.route('/kenttä/<icao_code>')
def airport_info(icao_code):
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        response = {
            "ICAO": icao_code,
            "Name": result["name"],
            "Municipality": result["municipality"]
        }
        status_code = 200
    else:
        response = {
            "error": "Airport not found"
        }
        status_code = 404

    json_response = json.dumps(response)
    return Response(response=json_response, status=status_code, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
