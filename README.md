# Tiwari AI Engineer

Python AI assistant for Termux: Gemini coding assistant, research summaries, and optional Google Sheets memory.

## Setup (Termux)
```bash
pkg update -y && pkg install python git -y
git clone https://github.com/coodwithyogesh-blip/ai-for-hacking-.git
cd ai-for-hacking-
pip install -r requirements.txt
cp .env.example .env
nano .env
python main.py
```
Enter your Gemini API key in .env. For Sheets memory, set Sheets ID and service-account JSON, share the Sheet with the service-account email.

Run `/learn` for research summary cycle. Android background restrictions and API quotas mean 24/7 operation requires an active host and supervision.

Security scope: authorized, defensive and isolated-lab activities only.
