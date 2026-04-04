import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestJoy(unittest.TestCase):
    def testJoy(self):
        text = 'I am glad this happened'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

class TestAnger(unittest.TestCase):
    def testAnger(self):
        text = 'I am really mad about this'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')

class TestDisgust(unittest.TestCase):
    def testDisgust(self):
        text = 'I feel disgusted just hearing about this'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

class TestSadness(unittest.TestCase):
    def testSadness(self):
        text = 'I am so sad about this'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

class TestFear(unittest.TestCase):
    def testFear(self):
        text = 'I am really afraid that this will happen'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')

unittest.main()