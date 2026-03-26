import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase): 
    def test_statement1(self):
        DOM_EMOTION = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(DOM_EMOTION, "joy")

    def test_statement2(self):
        DOM_EMOTION = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(DOM_EMOTION, "anger")

    def test_statement3(self):
        DOM_EMOTION = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(DOM_EMOTION, "disgust")

    def test_statement4(self):
        DOM_EMOTION = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(DOM_EMOTION, "sadness")

    def test_statement5(self):
        DOM_EMOTION = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(DOM_EMOTION, "fear")

unittest.main()