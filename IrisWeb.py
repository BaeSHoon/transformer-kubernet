# %%
"""
# URL : http://localhost:8080/cgi-bin/iris-web.py
"""
# 모듈 로딩 ---------------------------------------------------
import cgi, sys, codecs, os
from tensorflow.keras.models import load_model

file_name = "iris_model.h5"

# WEB 인코딩 설정 ---------------------------------------------
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
labels = {
    "Iris-setosa": [1, 0, 0],
    "Iris-versicolor": [0, 1, 0],
    "Iris-virginica": [0, 0, 1],
}

# 판정 --------------------------------------------------------
def detect_iris(s_l, s_w, p_l, p_w):
    x_new = [[float(s_l), float(s_w), float(p_l), float(p_w)]]
    y_pred = model.predict(x_new)

    # 판별 ------------------------------------
    _y = y_pred.tolist()[0]
    _y = [round(v) for v in _y]

    for key, value in list(labels.items()):
        if value == _y:
            return str(key)


# 기능 구현 -----------------------------------------------------
# (1) 모델 로딩 --------------------------------------------
model_file = os.path.dirname(__file__) + "/iris_model.h5"
model = load_model(model_file)

# (2) WEB 페이지 <Form> -> <INPUT> 리스트 가져오기
form = cgi.FieldStorage()
s_length_value = form.getvalue("s_length")
s_width_value = form.getvalue("s_width")
p_length_value = form.getvalue("p_length")
p_width_value = form.getvalue("p_width")

# (3) 판정 하기
def getValue():
    if (
        s_length_value is not None
        and s_width_value is not None
        and p_length_value is not None
        and p_width_value is not None
    ):
        result = detect_iris(
            s_length_value,
            s_width_value,
            p_length_value,
            p_width_value,
        )
        return result
    else:
        result = "측정된 결과가 없습니다."
        return result
