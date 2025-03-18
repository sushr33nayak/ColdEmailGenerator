# LLM Cold Email Generation using LLaMA 3.1 & ChatGroq

## Overview
This project leverages **LLaMA 3.1** with **ChatGroq** to automate and optimize cold email generation. It uses **Large Language Models (LLMs)** to craft personalized, high-quality outreach emails with minimal manual intervention. The system is designed for businesses, marketers, and sales teams looking to enhance their email engagement rates.

## Features
- **AI-Powered Cold Email Generation** using LLaMA 3.1
- **ChatGroq Integration** for efficient text generation
- **Dynamic Personalization** based on recipient data
- **Pre-built Email Templates** for different use cases
- **API Support** for seamless integration with CRM and email tools
- **Auto-Tuning & Optimization** for better email open and response rates

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Virtual Environment (optional but recommended)
- API access to ChatGroq

## Installation
Clone the repository:
```sh
cd your-repo
```

Create and activate a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

Install dependencies:
```sh
pip install -r requirements.txt
``````


## Configuration
Update the `config/settings.py` file to configure:
- **ChatGroq API Key**


## Running Tests
Run unit tests to validate functionality:
```sh
pytest tests/
```

## Deployment
To deploy as a web service:
```sh
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

