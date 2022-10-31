FROM python:3.10

LABEL version="0.1"
LABEL maintainer="jychpr - Joy Chrissetyo Prajogo"
LABEL release-date="2022-10-31"

WORKDIR /workstation

COPY final_requirements.txt final_requirements.txt
COPY dwh-coding-challenge dwh-coding-challenge

RUN pip install -r final_requirements.txt

