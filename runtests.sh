#! /bin/sh
coverage run -m pytest app/tests.py
coverage report -m
