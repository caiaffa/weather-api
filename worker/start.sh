#! /usr/bin/env bash
set -e

celery worker -A app.worker -l info -Q weather_queue -c 1
