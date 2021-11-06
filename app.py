# -*- coding: utf-8 -*-
"""flask app."""
from flask import Flask, render_template, request

from transformer import model, predict

app = Flask(__name__)


@app.route("/transformer", methods=["GET"])
def transformer():
    """
    load default transformer page.

    Returns:
        rendering html using flask
    """
    return render_template("transformer.html")


@app.route("/transformer", methods=["POST"])
def transformer_post():
    """
    POST data from sites.

    args:
        sentence    (str)   : recived data from html
        result      (str)   : `predict(str(sentence))` predict answer using transformer model

    Returns:
        render html using flask
    """
    sentence = request.form["sentence"]
    result_predict = predict(request.form["sentence"])
    return render_template("transformer.html", sentence=sentence, result=result_predict)


@app.route("/transformer/post", methods=["POST"])
def transformer_post_form():
    """
    POST data from requested.

    args
        sentence (str) : `sentence` value
        result   (str) : `predict(__str__)` transformer를 이용한 예측값

    Returns:
        json data
    """
    print(request.get_json()["sentence"])
    request.get_json()["transformer"] = predict(request.get_json()["sentence"])

    return request.get_json()


if __name__ == "__main__":
    model.load_weights("best_model.h5")
    app.run(host="0.0.0.0", port="5000")
