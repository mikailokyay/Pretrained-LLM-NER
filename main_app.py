from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
from utils import unify_tags

app = Flask(__name__)
model_name = "Davlan/bert-base-multilingual-cased-ner-hrl"

@app.route('/multilingual_ner_prediction', methods=['POST'])
def multilingual_ner_prediction():
    """
       NER prediction function
       :return: json
           output body
       """
    resp_json = request.get_json(force=True)
    failure_message = {
        "status": "Failure",
        "failure_reason": "Empty text"
    }

    try:
        if resp_json["text"] != "":
            recognized_entities = recognizer(resp_json["text"])
            unified_entities = unify_tags(recognized_entities)
            output = {
                    "predicted tags :": recognized_entities,
                    "unified tags :": unified_entities,
                }


        else:
            output = failure_message

        return jsonify(str(output))

    except KeyError as key_err:
        failure_message["failure_reason"] = str(key_err)

    return jsonify(failure_message)

if __name__ == '__main__':
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    recognizer = pipeline("ner", model=model, tokenizer=tokenizer)

    app.run(debug=True, host='0.0.0.0', port=5000)
