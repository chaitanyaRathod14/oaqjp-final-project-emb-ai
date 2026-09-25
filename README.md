# EmotionDetection

EmotionDetection is a Flask web application that identifies emotions in a sentence using the IBM Watson NLP Emotion Lite API.

## Technologies

- Python
- Flask
- requests
- IBM Watson NLP Emotion Lite API
- unittest

## Installation

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

If the Watson service is unavailable, enable the clearly labeled offline demo mode for local interface screenshots:

```powershell
$env:EMOTION_DEMO_MODE = "1"
py server.py
```

The normal Watson behavior is restored by closing the terminal or running:

```powershell
Remove-Item Env:EMOTION_DEMO_MODE
```

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
