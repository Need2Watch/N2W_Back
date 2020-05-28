[![Stargazers][stars-shield]](https://github.com/Need2Watch/N2W_Back/stargazers)
[![Issues][issues-shield]](https://github.com/Need2Watch/N2W_Back/issues)
[![MIT License][license-shield]](https://github.com/Need2Watch/N2W_Back/blob/master/LICENSE)

# Need2Watch Backend API

## Introduction

Need2Watch is a web application where you can keep a track of the Tv Series and Movies that you are following and watching

The backend of this application consist in an API REST.

## Usage

### Dependencies

- Docker
- Docker-Compose
- MySQL
- Virtualenv
- Python 3.7

### Steps

- Create a Python 3.7 Virtual environment
- Inside of the environment run `pip install -r requirements`
- Run `docker-compose up -d`
- Run `python create_db.py`
- Run `flask run`
- Access to `http://127.0.0.1:5000` and you will see the Swagger UI with all the API methods and you can test them.

#### Steps for Ubuntu and similar

- [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Install Docker-Compose](https://docs.docker.com/compose/install/)
- For installing the dependencies run `sudo apt install python3.7 python3.7-dev virtualenv build-essential mysql-server mysql-client libmysqlclient-dev libsqlclient-dev libssl-dev`
- To create the virtualenvironment run `virtualenv -p python3.7 venv`
- To activate it run `source venv/bin/activate`
- Then run the commands specified above `pip install -r requirements`
- Run `docker-compose up -d`
- Run `python create_db.py`
- Run `flask run`
- Access to `http://127.0.0.1:5000` and you will see the Swagger UI with all the API methods and you can test them.


<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Need2Watch/N2W_Back
[forks-shield]: https://img.shields.io/github/forks/Need2Watch/N2W_Back
[stars-shield]: https://img.shields.io/github/stars/Need2Watch/N2W_Back
[issues-shield]: https://img.shields.io/github/issues/Need2Watch/N2W_Back
[license-shield]: https://img.shields.io/github/license/Need2Watch/N2W_Back