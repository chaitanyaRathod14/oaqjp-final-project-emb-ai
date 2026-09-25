
# Emotion Detector

## Project Overview

This project is an Emotion Detector application developed using Python and Flask.

The application analyzes a given text and detects the emotions expressed in the text using the Watson NLP Emotion Detection service.

The detected emotions are:

- Anger
- Disgust
- Fear
- Joy
- Sadness

The application also identifies the **dominant emotion** based on the highest emotion score.

## Project Structure

```text
Emotion-Detector/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
