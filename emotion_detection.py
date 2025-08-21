import requests
import json

# Define the Watson NLP API endpoint and headers
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """
    Sends the text to Watson NLP EmotionPredict API
    and returns the JSON response containing detected emotions.
    """
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send POST request to Watson NLP API
        response = requests.post(URL, headers=HEADERS, json=input_json)

        # Raise an error if the request fails
        response.raise_for_status()

        # Return the JSON response content
        return response.text

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)})
