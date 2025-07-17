"""
# 🧠 GenAI Medical Summary Generator

This project takes raw radiology or medical text and summarizes it using OpenAI's GPT-3.5 Turbo.

## 🔧 Features
- REST API with FastAPI
- GPT-powered summary generation
- Dockerized for portability
- AWS EC2 deployment ready
- GitHub Actions CI pipeline

## 📦 Usage
```bash
# Run locally
uvicorn app.main:app --reload
```

### Example input:
```json
{"input_text": "Patient presents with symptoms of chronic sinusitis. CT shows mucosal thickening..."}
```

### Example output:
```json
{"summary": "The patient likely suffers from chronic sinusitis as shown by CT imaging..."}
```

## ☁️ Deploy on AWS EC2
```bash
# SSH into instance and clone this repo
sudo apt install docker.io
sudo docker build -t genai-app .
sudo docker run -d -p 80:80 genai-app
```

## 📚 API Docs
Once running:
http://localhost:8000/docs

"""
