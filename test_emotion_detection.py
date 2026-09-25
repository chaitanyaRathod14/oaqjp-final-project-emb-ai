"""Unit tests for the EmotionDetection application function."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test dominant emotion selection with mocked Watson responses."""

    def _mock_response(self, dominant_emotion):
        scores = {
            "anger": 0.05,
            "disgust": 0.05,
            "fear": 0.05,
            "joy": 0.05,
            "sadness": 0.05,
        }
        scores[dominant_emotion] = 0.8
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"emotionPredictions": [{"emotion": scores}]}
        return response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value = self._mock_response("joy")
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value = self._mock_response("anger")
        self.assertEqual(emotion_detector("I am really angry about this")["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        mock_post.return_value = self._mock_response("disgust")
        self.assertEqual(emotion_detector("This is disgusting")["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_post.return_value = self._mock_response("sadness")
        self.assertEqual(emotion_detector("I am very sad")["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        mock_post.return_value = self._mock_response("fear")
        self.assertEqual(emotion_detector("I am afraid")["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request_returns_empty_result(self, mock_post):
        response = Mock(status_code=400)
        mock_post.return_value = response
        result = emotion_detector("invalid input")
        self.assertTrue(all(value is None for value in result.values()))

    def test_blank_input_returns_empty_result(self):
        result = emotion_detector("   ")
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()