from chalice import BadRequestError, Chalice
from nltk import ngrams

app = Chalice(app_name="ngrammer")


@app.route("/")
def test() -> dict:
    return {"hello": "world"}


@app.route("/ngrammer", methods=["POST"])
def ngrammer() -> dict:
    json_input = app.current_request.json_body
    try:
        order = int(json_input["order"])
        text = json_input["text"]
        result = [i for i in ngrams(text.split(), order)]
        return {"order": order, "ngrams": result}
    except KeyError:
        raise BadRequestError("Request body must contain these 2 keys: 'order', 'text'")
    except Exception as e:
        raise BadRequestError(e)
