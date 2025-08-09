## Python Flask CI/CD Demo

This project is a simple Python Flask web application with automated testing and Docker-based CI/CD using Jenkins.

### Features
- Flask web app with login, profile, and home pages
- Automated tests with pytest
- Dockerized for easy deployment
- Jenkins pipeline for CI/CD

### Project Structure
- `app.py` — Main Flask application
- `templates/` — HTML templates (home, login, profile)
- `test_app.py` — Pytest test cases
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker build instructions
- `Jenkinsfile` — Jenkins pipeline definition

### Setup & Run Locally
1. Clone the repository:
	```bash
	git clone https://github.com/PrajwalMalokar/jenkins-ci-cd-practice.git
	cd jenkins-ci-cd-practice
	```
2. Create a virtual environment and install dependencies:
	```bash
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	```
3. Run the Flask app:
	```bash
	python app.py
	```

### Run Tests
```bash
pytest
```

### Build & Run with Docker
```bash
docker build -t flask-demo .
docker run -p 5000:5000 flask-demo
```

### CI/CD Pipeline
- Jenkins is configured to build, test, and (optionally) deploy the Docker image on every push to GitHub using the `Jenkinsfile`.
- Webhook triggers Jenkins automatically.

---
Feel free to modify and extend!
