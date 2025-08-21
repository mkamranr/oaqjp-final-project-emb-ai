import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):    
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:        
        response = requests.post(URL, headers=HEADERS, json=input_json)
        response.raise_for_status()        
        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]

        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)        
        emotion_scores = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
