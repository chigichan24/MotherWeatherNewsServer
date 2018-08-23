from EmotionEstimator import face_to_emotion,text_to_emotion

assert(face_to_emotion(image_path='sample/face1.png') == {'anger': 0.013, 'contempt': 0.002, 'disgust': 0.0, 'fear': 0.001, 'happiness': 0.0, 'neutral': 0.611, 'sadness': 0.372, 'surprise': 0.0})
assert(text_to_emotion("今日はとてもいい天気だなぁ") == {'magnitude': 0.699999988079071, 'score': 0.699999988079071})
