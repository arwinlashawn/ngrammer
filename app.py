from chalice import Chalice
from nltk import ngrams

app = Chalice(app_name="ngrammer")


@app.route("/")
def test() -> dict:
    return {"hello": "world"}


@app.route("/ngrammer", methods=["POST"])
def ngrammer() -> dict:
    # to do: implement error handling
    json_input = app.current_request.json_body
    order = json_input["order"]
    text = json_input["text"]
    result = {i for i in ngrams(text.split(), order)}

    return {"order": order, "ngrams": result}
