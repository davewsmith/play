#!/bin/bash

venv/bin/celery -A server.celery worker
