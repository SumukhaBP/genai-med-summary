"""
# 🧠 GenAI Medical Summary Generator (HuggingFace Edition)

This project takes raw radiology or medical text and summarizes it using a free open-source HuggingFace transformer model (`facebook/bart-large-cnn`).

## 🔧 Features
- REST API with FastAPI
- HuggingFace BART-based summarization
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
{"summary": "The patient has chronic sinusitis with mucosal thickening shown on CT..."}
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
