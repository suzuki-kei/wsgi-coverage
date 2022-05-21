FROM httpd:2.4

RUN apt-get update && apt-get install -y --no-install-recommends \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip

COPY ./src /opt/wsgi-coverage-app

COPY ./config/httpd-wsgi-coverage-app.conf /usr/local/apache2/conf/extra/
RUN sed -i '$a Include conf/extra/httpd-wsgi-coverage-app.conf' /usr/local/apache2/conf/httpd.conf

