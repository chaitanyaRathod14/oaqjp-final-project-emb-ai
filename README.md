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
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```