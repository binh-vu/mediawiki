FROM mediawiki:1.37

RUN apt update -y
RUN apt install -y ploticus fonts-freefont-ttf

ADD extensions /tmp/extensions

RUN cd /var/www/html/extensions && \
    tar -xzf /tmp/extensions/timeline-REL1_37-94b7a42.tar.gz -C /var/www/html/extensions/ && \
    tar -xzf /tmp/extensions/TemplateData-REL1_37-e89d05e.tar.gz -C /var/www/html/extensions/

RUN rm -rf /tmp/extensions