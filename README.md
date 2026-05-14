# sentinelFS

SentinelFS is a Linux filesystem integrity enforcement tool that monitors protected directories and automatically removes unauthorized files in real time.

The project is designed to explore:
- Linux filesystem monitoring
- security automation
- event-driven programming
- filesystem integrity enforcement
- DevOps-oriented infrastructure tooling

---

# Features

- Real-time filesystem monitoring
- Unauthorized file detection
- Automatic file removal
- Whitelist-based enforcement
- Linux inotify integration via watchdog
- YAML-based policy configuration

---

# Architecture

```text
Filesystem Event
       ↓
SentinelFS Observer
       ↓
Whitelist Validation
       ↓
Unauthorized File Removal
```

---

# Project Structure

```text
sentinelfs/
├── src/
│   ├── main.py
│   └── logger.py
│
├── config/
│   └── policy.yaml
│
├── protected/
│   └── allowed.txt
│
├── logs/
│   └── sentinelfs.log
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone <repo-url>
cd sentinelfs
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run SentinelFS:

```bash
python3 src/main.py
```

Create a test file:

```bash
touch protected/test.sh
```

Unauthorized files will be automatically removed.

---

# Tech Stack

- Python
- Linux
- watchdog
- inotify
- Git

---

# Roadmap

- YAML configuration support
- Logging system
- systemd service integration
- Docker support
- CI/CD pipeline
- Prometheus metrics
- Grafana dashboard integration

---

# License

MIT License
