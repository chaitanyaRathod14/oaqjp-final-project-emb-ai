# EmotionDetection

EmotionDetection is a simple Flask web application for identifying the dominant emotion in a sentence with the IBM Watson NLP Emotion Lite API.

## Technologies

- Python
- Flask
- requests
- IBM Watson NLP Emotion Lite API
- unittest

## Installation

From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Run the application

```powershell
py server.py
```

Open <http://127.0.0.1:5000> in a browser.

## Run the tests

```powershell
py -m unittest -v test_emotion_detection.py
```

## Run pylint

```powershell
py -m pylint server.py
```

## Project structure

```text
EmotionDetection/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
=======

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
>>>>>>> origin/main
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```
