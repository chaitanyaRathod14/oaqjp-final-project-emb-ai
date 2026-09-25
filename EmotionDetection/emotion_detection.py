"""Emotion detection using the Watson NLP Emotion Lite service."""

from typing import Any, Dict, Optional

import requests


API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.emotion-lite-v1"
)
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result() -> Dict[str, Optional[Any]]:
    """Return the standard result shape for an unavailable analysis."""
    result = {emotion: None for emotion in EMOTIONS}
    result["dominant_emotion"] = None
    return result


def emotion_detector(text_to_analyze: str) -> Dict[str, Optional[Any]]:
    """Return emotion scores and the dominant emotion for a sentence."""
    if not text_to_analyze or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
    except requests.RequestException:
        return _empty_result()

    if response.status_code == 400:
        return _empty_result()
    if response.status_code != 200:
        return _empty_result()

    response_data = response.json()
    emotion_data = response_data.get("emotionPredictions", [{}])[0].get(
        "emotion", {}
    )
    if not all(emotion in emotion_data for emotion in EMOTIONS):
        return _empty_result()

    result = {emotion: emotion_data[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(
        EMOTIONS, key=lambda emotion: emotion_data[emotion]
    )
    return result