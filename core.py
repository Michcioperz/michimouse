#!/usr/bin/env python2
from flask import Flask, render_template, g, json
import argparse

app = Flask(__name__)
app.config.update(DEBUG = True, SERVER_NAME = '0.0.0.0:8765', MICHIMOUSE_HOOKS = [])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Micromouse robot debug server")
    parser.add_argument('-b', '--bind', type = str, help = "A hostname and a port for the webserver core")
    args = parser.parse_args()
    if 'bind' in args:
        app.config.update(SERVER_NAME = args.bind)
    app.run()
