from flask import Flask
from random import Random

app = Flask(__name__)


@app.route("/metrics")
def hello():
    random = Random()
    number_of_users_frontend = random.randint(10, 20)
    number_of_users_backend = random.randint(10, 20)

    return f"""
    # Metrics in prometheus format
    number_of_users{{service="myapp",application="frontend"}} {number_of_users_frontend}
    number_of_users{{service="myapp",application="backend"}} {number_of_users_backend}
    """


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
