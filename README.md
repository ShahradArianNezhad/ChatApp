# Django Chat App with WebSockets

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=websocket&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

A real-time chat application built with Django and WebSockets (Channels) that supports user registration, chatroom creation, and profile customization.

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
- Redis (for channel layer in production)

## Installation

### Without Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-chat-app.git
   cd django-chat-app