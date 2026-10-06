<div align="center">

# 🧙‍♂️ WIZARD MUSIC BOT

### 🎵 Modern Telegram Music Bot • Voice Chat • Queue • Player Controls

<p>
  <img src="https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  <img src="https://img.shields.io/badge/PyTgCalls-2.3.3-blue?style=for-the-badge" alt="PyTgCalls">
  <img src="https://img.shields.io/badge/yt--dlp-modern-red?style=for-the-badge" alt="yt-dlp">
</p>

<p>
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/YOUR_USERNAME/Wizard-Music-Bot?style=for-the-badge&logo=github" alt="Stars">
  </a>
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/network/members">
    <img src="https://img.shields.io/github/forks/YOUR_USERNAME/Wizard-Music-Bot?style=for-the-badge&logo=github" alt="Forks">
  </a>
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/issues">
    <img src="https://img.shields.io/github/issues/YOUR_USERNAME/Wizard-Music-Bot?style=for-the-badge" alt="Issues">
  </a>
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/YOUR_USERNAME/Wizard-Music-Bot?style=for-the-badge" alt="License">
  </a>
</p>

<p>
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/stargazers">⭐ Star</a>
  •
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/fork">🍴 Fork</a>
  •
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/issues">🐛 Report Bug</a>
  •
  <a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/issues/new">💡 Request Feature</a>
</p>

</div>

---

## 🖼️ Preview

> Add your actual screenshots to `assets/screenshots/` and replace the filenames below.

<div align="center">

<img src="./assets/screenshots/banner.png" alt="Wizard Music Bot Banner" width="900">

</div>

### 🎵 Player

<div align="center">

<img src="./assets/screenshots/player.png" alt="Wizard Music Bot Player" width="500">

</div>

### 🎛️ Player Controls

<div align="center">

<img src="./assets/screenshots/controls.png" alt="Wizard Music Bot Controls" width="500">

</div>

### 📋 Queue

<div align="center">

<img src="./assets/screenshots/queue.png" alt="Wizard Music Bot Queue" width="500">

</div>

---

# ✨ About

**Wizard Music Bot** is a modern Telegram music bot designed for high-quality voice-chat playback.

It provides a clean player experience with queue management, interactive controls, media searching, looping and automatic playback.

The project uses a modular architecture so features can be added without rewriting the entire application.

---

# ⚡ Features

| Feature                     | Status |
| --------------------------- | :----: |
| 🎵 Music playback           |    ✅   |
| 🔎 YouTube search           |    ✅   |
| 🎧 Voice chat streaming     |    ✅   |
| 📋 Queue system             |    ✅   |
| ⏭️ Skip                     |    ✅   |
| ⏸️ Pause / Resume           |    ✅   |
| 🔁 Loop                     |    ✅   |
| ⏹️ Stop                     |    ✅   |
| 🎛️ Inline player controls  |    ✅   |
| 👑 Multiple owners          |    ✅   |
| 🍪 Optional YouTube cookies |    ✅   |
| 🐳 Docker                   |    ✅   |
| ☁️ Railway deployment       |    ✅   |
| 🐍 Python 3.14 support      |    ✅   |
| 🧩 Plugin architecture      |    ✅   |

---

# 🧙 Why Wizard?

Wizard was created to provide a clean and maintainable alternative to older Telegram music-bot codebases.

### Designed for:

* ⚡ Fast startup
* 🎧 Reliable voice playback
* 🧩 Modular plugins
* 🔐 Secure environment configuration
* ☁️ Container deployment
* 🛠️ Easy customization
* 📈 Future feature expansion

---

# 📸 Screenshots

Store screenshots inside:

```text
assets/
└── screenshots/
    ├── banner.png
    ├── player.png
    ├── controls.png
    ├── queue.png
    └── settings.png
```

GitHub supports repository-relative image paths, so these images will continue to work when users clone or fork the repository.

---

# 🚀 Installation

## Requirements

* Python 3.14+
* FFmpeg
* Node.js 22+
* Telegram API credentials
* Telegram Bot Token
* Assistant session
* Optional YouTube cookies

---

## Clone

```bash
git clone https://github.com/YOUR_USERNAME/Wizard-Music-Bot.git

cd Wizard-Music-Bot
```

## Virtual Environment

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## Install

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

Copy:

```bash
cp .env.example .env
```

Configure:

```env
API_ID=
API_HASH=
BOT_TOKEN=

OWNER_ID=
OWNER_IDS=

STRING_SESSION=

DURATION_LIMIT=60

YTDLP_COOKIES_B64=
```

### 🔐 Never commit `.env`

Your repository should never contain:

```text
.env
cookies.txt
*.session
session.txt
```

---

# ▶️ Start

```bash
python -m wizard
```

---

# 🎵 Commands

| Command          | Function             |
| ---------------- | -------------------- |
| `/play <query>`  | Play a song          |
| `/vplay <query>` | Play supported video |
| `/pause`         | Pause                |
| `/resume`        | Resume               |
| `/skip`          | Skip current track   |
| `/loop`          | Toggle loop          |
| `/stop`          | Stop playback        |
| `/queue`         | Show queue           |

---

# 🎛️ Interactive Player

Wizard also provides an interactive player interface.

```text
┌──────────────────────────────┐
│        🎵 NOW PLAYING        │
│                              │
│       Song Name              │
│       Artist Name            │
│                              │
│  ⏸ Pause    ⏭ Skip           │
│  🔁 Loop     ⏹ Stop          │
└──────────────────────────────┘
```

---

# 📋 Queue System

Multiple songs can be requested without interrupting the current track.

Example:

```text
/play song 1
/play song 2
/play song 3
/play song 4
```

Wizard maintains the queue and automatically moves to the next track when playback finishes.

---

# 🔁 Loop

Loop support allows the current track to repeat according to the configured player behavior.

```text
/loop
```

The player controls also expose loop functionality.

---

# 🐳 Docker

Build:

```bash
docker build -t wizard-music-bot .
```

Run:

```bash
docker run --env-file .env wizard-music-bot
```

---

# ☁️ Railway

Wizard is suitable for container-based deployment.

### Steps

1. Fork the repository.
2. Create a Railway project.
3. Connect the GitHub repository.
4. Add environment variables.
5. Deploy.
6. Check logs.
7. Test `/play`.

### Environment variables

```text
API_ID
API_HASH
BOT_TOKEN
OWNER_ID
OWNER_IDS
STRING_SESSION
DURATION_LIMIT
YTDLP_COOKIES_B64
```

---

# 🏗️ Architecture

```text
                  ┌─────────────────┐
                  │     Telegram    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │      Wizard     │
                  │   Bot Client    │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         ┌─────────┐  ┌──────────┐  ┌─────────┐
         │ Plugins │  │  Queue   │  │ Config  │
         └────┬────┘  └────┬─────┘  └─────────┘
              │            │
              └──────┬─────┘
                     ▼
              ┌──────────────┐
              │   yt-dlp     │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   PyTgCalls  │
              └──────┬───────┘
                     │
                     ▼
              🔊 Telegram VC
```

---

# 📁 Project Structure

```text
Wizard-Music-Bot/
│
├── wizard/
│   ├── core/
│   ├── plugins/
│   ├── config.py
│   └── __main__.py
│
├── assets/
│   └── screenshots/
│
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── README.md
```

---

# 🧪 Development

Check Python compilation:

```bash
python -m compileall wizard
```

Run:

```bash
python -m wizard
```

---

# 🤝 Contributing

Contributions are welcome.

```text
Fork
  ↓
Create branch
  ↓
Make changes
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Pull Request
```

Example:

```bash
git checkout -b feature/my-feature

git add .

git commit -m "Add my feature"

git push origin feature/my-feature
```

---

# 🐛 Bug Reports

Please include:

```text
Python version:
Wizard version:
Deployment platform:
Operating system:
Error:
Logs:
Steps to reproduce:
```

### Never include

```text
BOT_TOKEN
API_HASH
STRING_SESSION
Cookies
Passwords
Private API keys
```

---

# 💡 Feature Requests

Open an issue and explain:

* What you want
* Why it is useful
* How it should work
* Example usage
* Any screenshots or references

---

# 🔐 Security

If you discover a security vulnerability, do **not** publish credentials or exploit details in a public issue.

Instead, use the repository's security reporting process.

Recommended repository files:

```text
SECURITY.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
LICENSE
```

---

# ⚖️ Copyright

Copyright © 2026 **Wizard Music Bot Contributors**

All rights reserved except where a specific license or third-party license states otherwise.

Wizard may contain or depend upon third-party open-source software. Their respective copyrights and licenses remain with their original authors.

---

# 📜 License

See [`LICENSE`](LICENSE) for the complete license terms.

Third-party dependencies remain subject to their respective licenses.

---

# ⚠️ Disclaimer

Wizard Music Bot is provided **"AS IS"**, without warranties of any kind.

The maintainers are not responsible for:

* misuse of the software;
* copyright infringement;
* unauthorized access to accounts;
* misuse of Telegram sessions;
* misuse of third-party services;
* media downloaded or streamed by users;
* service interruptions;
* API changes;
* data loss;
* leaked credentials;
* violations of applicable laws or service terms.

Users are responsible for how they configure and operate the software.

---

# 🎵 Copyright & Media

Wizard does not claim ownership of music, videos, thumbnails, artwork or other media retrieved through third-party services.

Users are responsible for ensuring that their use of media complies with applicable copyright laws and the terms of the services they use.

---

# ❤️ Credits

Built with the open-source ecosystem:

* 🐍 Python
* 📱 Telegram
* 🔊 PyTgCalls
* 🔎 yt-dlp
* 🎞️ FFmpeg
* 🟢 Node.js

Special thanks to all developers, contributors and testers who make open-source Telegram projects possible.

---

# ⭐ Support Wizard

If you like Wizard, consider supporting the project:

<p align="center">

<a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/stargazers">
<img src="https://img.shields.io/badge/⭐%20Star%20the%20Repository-yellow?style=for-the-badge">
</a>

<a href="https://github.com/YOUR_USERNAME/Wizard-Music-Bot/fork">
<img src="https://img.shields.io/badge/🍴%20Fork%20Wizard-blue?style=for-the-badge">
</a>

</p>

### Every star helps ⭐

If Wizard helped you, consider giving the repository a star.

---

<div align="center">

## 🧙 Made with ❤️ for Telegram

**Wizard Music Bot © 2026**

⭐ Star • 🍴 Fork • 🐛 Report • 💡 Contribute

</div>
