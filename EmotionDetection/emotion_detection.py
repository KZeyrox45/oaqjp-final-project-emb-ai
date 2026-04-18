import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=headers)

    # Handle response status code
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # Extract anger, disgust, fear, joy and sadness, along with their scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        # Find the dominant_emotion which has the highest score in emotions
        dominant_emotion = max(emotions, key=emotions.get)
    # If the status code is 400, set all values to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    # For any unexpected status code, set all values to None
    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    # Return the response text from the API
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
