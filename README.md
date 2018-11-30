# Trasher Bot

> Prototype project for ForCity

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![Build Status](https://travis-ci.com/yoyonel/forcity_trasherbot.svg?branch=master)](https://travis-ci.com/yoyonel/forcity_trasherbot)

## Instructions

Structure is based on [this article](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure). Source code can be found in the `src` folder, and tests in the `tests` folder.

To install the package, simply execute

```bash
➤ pip install -r requirements_dev.txt
```

We use `tox` for the tests. This ensure a clear separation between the development environment and the test environment.
To launch the tests, run the `tox` command:

```bash
➤ tox
```

It first starts with a bunch of checks (`flask8` and others) and then launch the tests using python 3.

## Packaging

A Dockerfile is provided to build an image ready to be deployed, see `docker/Dockerfile`. You can build the image using `make`:

```bash
➤ make docker
```

This will create a new image named ``.

# PyPi: Docker container for PyPi server

## Run

### On Windows with Docker

```cmd
λ docker build -t yoyonel/forcity_trasherbot:0.9.0 -f docker\Dockerfile  .
...
Successfully built 14c63bf8a20f
Successfully tagged yoyonel/forcity_trasherbot:0.9.0

[...]\forcity_trasherbot (master -> origin)
λ docker run -it --rm -v %cd%/data:/data yoyonel/forcity_trasherbot:0.9.0 /data/config_00.json
2018-12-02 00:04:34,185 - forcity.trasherbot.app - INFO - application version: 0.9.0
2018-12-02 00:04:34,188 - forcity.trasherbot.simulator - INFO - init game: trash pop, remaining 1
2018-12-02 00:04:34,189 - forcity.trasherbot.simulator - INFO - init game: trash pop, remaining 2
2018-12-02 00:04:34,189 - forcity.trasherbot.simulator - INFO - init game: trash pop, remaining 3
2018-12-02 00:04:34,189 - forcity.trasherbot.simulator - INFO - Round 2/50: trash collected, remaining 2
2018-12-02 00:04:34,189 - forcity.trasherbot.simulator - INFO - Round 4/50: trash collected, remaining 1
2018-12-02 00:04:34,190 - forcity.trasherbot.simulator - INFO - Round 4/50: trash pop, remaining 2
2018-12-02 00:04:34,190 - forcity.trasherbot.simulator - INFO - Round 5/50: trash collected, remaining 1
2018-12-02 00:04:34,190 - forcity.trasherbot.simulator - INFO - Round 6/50: trash collected, remaining 0
2018-12-02 00:04:34,190 - forcity.trasherbot.simulator - INFO - success. Collected all trashes in 6 rounds
```

## Screencast (Asciinema)

[![asciicast]()
