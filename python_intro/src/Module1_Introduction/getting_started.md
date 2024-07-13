# English

# Getting Started

## 1. Set Up Your Environment

Creating a virtual environment helps you manage project dependencies separately from your system Python installation.

### Windows

1. Open Terminal or PowerShell.
2. Navigate to your project directory:
   ```bash
   cd path\to\your\project\python_intro
   ```
3. Create a virtual environment:
   python -m venv env
4. Activate the virtual environment:
   .\env\Scripts\activate

### Mac | Linux (Ubuntu)

1. Open Terminal
2. Navigate to your project directory:
   cd path/to/your/project/python_intro

3. Create a virtual environment:
   python3 -m venv env

4. Activate the virtual environment
   source env/bin/activate

## 2. Installing Python (if you don't already have it)

### Windows

1. Download the installer from the official https://www.python.org/downloads/.
2. Run the installer and make sure to check the box that says "Add Python to PATH".
3. Follow the installation instructions.

### Mac

1. check if you have it:
   python3 --version

2. If not installed, you can use Homebrew to install Python. First, install Homebrew if you haven’t:
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

3. install python:
   brew install python

### Linux (Ubuntu)

1. check if you have it:
   python3 --version

2. if you don't have it, open a terminal and paste this commands:
   sudo apt update
   sudo apt install python3 python3-venv python3-pip

---

# Español

# Comenzando

## 1. Configura Tu Entorno

Crear un entorno virtual te ayuda a gestionar las dependencias del proyecto por separado de la instalación de Python de tu sistema.

### Windows

1. Abre la Terminal o PowerShell.
2. Navega a tu directorio del proyecto:
   ```bash
   cd path\to\your\project\python_intro
   ```
3. Crea un entorno virtual:
   python -m venv env
4. Activa el entorno virtual:
   .\env\Scripts\activate

### Mac | Linux (Ubuntu)

1. Abre la Terminal.
2. Navega a tu directorio del proyecto:
   cd path/to/your/project/python_intro

3. Crea un entorno virtual:
   python3 -m venv env

4. Activa el entorno virtual:
   source env/bin/activate

## 2. Instalando Python (si no lo tenés ya)

### Windows

1. Descarga el instalador desde el sitio oficial: https://www.python.org/downloads/.
2. Ejecuta el instalador y asegúrate de marcar la casilla que dice "Add Python to PATH".
3. Seguí las instrucciones de instalación.

### Mac

1. Verifica si ya lo tenés:
   python3 --version

2. Si no está instalado, podés usar Homebrew para instalar Python. Primero, instalá Homebrew si no lo has hecho:
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

3. Instala Python:
   brew install python

### Linux (Ubuntu)

1. Verificá si ya lo tenés:
   python3 --version

2. Si no lo tenés, abrí una terminal y pegá estos comandos:
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
