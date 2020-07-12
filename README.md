[![Stargazers][stars-shield]](https://github.com/Need2Watch/N2W_Back/stargazers)
[![Issues][issues-shield]](https://github.com/Need2Watch/N2W_Back/issues)
[![GPL3 License][license-shield]](https://github.com/Need2Watch/N2W_Back/blob/master/LICENSE)

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

1. Create a Python 3.7 Virtual environment
1. Inside of the environment run `pip install -r requirements`
1. Run `docker-compose up -d`
1. Create a .env file and set `DB_ENGINE` and `MOVIE_API_KEY` from [TMDB](https://www.themoviedb.org/settings/api)
1. Run `python create_db.py`
1. Run `flask run`
1. Access to `http://127.0.0.1:5000` and you will see the Swagger UI with all the API methods and you can test them.

#### Specific steps for Ubuntu and similar

1. [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
1. [Install Docker-Compose](https://docs.docker.com/compose/install/)
1. Install all the dependencies running `sudo apt install python3.7 python3.7-dev virtualenv build-essential mysql-server mysql-client libmysqlclient-dev libsqlclient-dev libssl-dev -y`
1. Create the virtual environment with `virtualenv -p python3.7 venv`
1. Activate it running `source venv/bin/activate`
1. Follow the [steps specified above](https://github.com/Need2Watch/N2W_Back#steps)

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Need2Watch/N2W_Back
[forks-shield]: https://img.shields.io/github/forks/Need2Watch/N2W_Back
[stars-shield]: https://img.shields.io/github/stars/Need2Watch/N2W_Back
[issues-shield]: https://img.shields.io/github/issues/Need2Watch/N2W_Back
[license-shield]: https://img.shields.io/github/license/Need2Watch/N2W_Back
