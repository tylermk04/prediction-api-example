import os

from flask import Flask, request, render_template
from flask.views import MethodView

import requests

app = Flask(__name__)

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", 6168)

class MpgView(MethodView):

    def get(self):
        return render_template("form.html")
    
    def post(self):
        cyl = request.form.get("cyl")
        disp = request.form.get("disp")
        hp = request.form.get("hp")
        mpg = self.__predict_mpg(cyl, disp, hp)
        if mpg:
            return render_template("form.html", predicted_mpg=mpg)
        return "Unable to predict horsepower, please try again."

    def __predict_mpg(self, cyl, disp, hp):
        body = {
            "cyl": int(cyl),
            "disp": int(disp),
            "hp": int(hp)
        }
        print("sending covariates for prediction: %s" % body)
        r = requests.post(f"http://{API_HOST}:{API_PORT}/predict", json=body)
        if r.status_code == 200:
            return r.json().get("mpg")[0]
        print("Got status %s from prediction api" % r.status_code)
        print(r.text)
        return None



app.add_url_rule("/", view_func=MpgView.as_view('mpg'))

if __name__ == "__main__":
    app.run(debug=True)