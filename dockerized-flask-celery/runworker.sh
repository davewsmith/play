#!/bin/bash

celery -A server.celery worker
