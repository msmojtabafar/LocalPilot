# LocalPilot

**Local AI Assistant for your computer.**

LocalPilot is an open-source local AI assistant designed to interact with your computer through controlled, secure, and extensible tools.

## Project Status

🚧 **Early Development**

The project is currently in its initial development stage.

## Planned Features

* 🤖 Local AI assistant
* 📁 File management
* 💻 Terminal interaction
* 🖥️ System information
* ⚙️ Process management
* 📦 Application management
* 🌐 Web access
* 🔌 Extensible tool system
* 🔗 MCP integration
* 🔐 Permission and security system
* 🧪 Automated testing

## Architecture

The project is being designed around a modular architecture so that new tools and capabilities can be added without tightly coupling them to the core assistant.

## Development

### Requirements

* Python 3.13+
* Linux
* Git

### Setup

Clone the repository:

```bash
git clone git@github.com:msmojtabafar/LocalPilot.git
cd LocalPilot
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 src/localpilot/main.py
```

Run tests:

```bash
pytest
```
