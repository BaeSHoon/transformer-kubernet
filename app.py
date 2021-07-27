# -*- coding: utf-8 -*-
"""flask app."""
from flask import Flask, render_template, request

from transformer import model, predict

app = Flask(__name__)


@app.route("/transformer", methods=["GET"])
def transformer():
    """
    초기 html 로드.

    Returns:
        rendering html using flask
    """
    return render_template("transformer.html")


@app.route("/transformer", methods=["POST"])
def transformer_post():
    a0 = request.form["a0"]
    result = predict(a0)
    return render_template("transformer.html", a0=a0, result=result)


@app.route("/transformer/post", methods=["POST"])
def transformer_post_form():
    """
    POST data from requested.

    args
        sentence (str) : `sentence` 의 value값
        run (str)      : `predict(str(sentence))` transformer를 이용한 예측값

    Returns:
        트랜스포머 모델로 출력
    """
    sentence = str(request.form["sentence"])

    return predict(sentence)


if __name__ == "__main__":
    # Load model
    model.load_weights("best_model.h5")
    app.run(host="127.0.0.1", port="5000")
