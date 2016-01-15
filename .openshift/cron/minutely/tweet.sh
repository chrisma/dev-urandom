#!/bin/bash

date >> ${OPENSHIFT_PYTHON_LOG_DIR}/tweet.log

python ${OPENSHIFT_REPO_DIR}/tweet.py
