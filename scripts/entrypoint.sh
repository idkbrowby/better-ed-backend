#!/bin/bash

poetry run uvicorn src.app:app --host 0.0.0.0 --reload --reload-dir ./src