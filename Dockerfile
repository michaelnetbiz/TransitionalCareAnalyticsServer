# TODO: add workflow for deploying with docker
# TODO: refactor project as library to include in implementation (dashboard) along with webpack-ized ng client
FROM continuumio/miniconda3

LABEL version="0.2"

LABEL description="Image for tcas containers"

RUN mkdir -p /var/log/gunicorn && touch /var/log/gunicorn/gunicorn.log && chmod 0777 /var/log/gunicorn/gunicorn.log

ADD ./environment.prod.yml /opt/project/environment.yml

RUN conda update conda -y && conda env create -f /opt/project/environment.yml

ENV PATH /opt/conda/envs/tcas/bin:$PATH

ADD ./data /opt/project/data

ADD ./app /opt/project/app

ADD ./wsgi.py /opt/project/wsgi.py

ADD ./ga_service_account_credentials.json /opt/project/ga_service_account_credentials.json

WORKDIR /opt/project/

RUN useradd -m postgres

USER postgres

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app --log-file /var/log/gunicorn/gunicorn.log --log-level info
