# Django Chat App with WebSockets

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=websocket&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Daphne](https://img.shields.io/badge/Daphne-6DA55F?style=for-the-badge&logo=django&logoColor=white)

A real-time chat application built with Django and WebSockets (Channels) and daphne that supports user registration, chatroom creation, and profile customization.

## Features

- **Real-time messaging** using Django Channels and WebSockets
- **User authentication** (register, login, logout)
- **Profile customization** with profile pictures
- **Chatroom creation** and management
- **Docker support** for easy deployment
- Responsive design

## Prerequisites

- Python 3.8+
- Docker (optional)

## Installation

### Without Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-chat-app.git
   cd django-chat-app

2. Create and activate a virtual environment:   
    ```bash
   pip install -r requirements.txt

4. Apply migrations:
    ```bash
    python manage.py migrate

5. Run the dev server(admin users password is admin)
    ```bash
    python manage.py runserver

### With Docker

1. Build the image:
    ```bash
    sudo docker build -t python-chatroom .

2. run the container:
    ```bash
    sudo docker run -p 8000:8000 --name my_app python-chatroom

the app will be available at http://localhost:8000

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.