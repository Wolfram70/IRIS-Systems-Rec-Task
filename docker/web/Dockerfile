FROM nginx

RUN apt-get update -qq && apt-get -y install apache2-utils

ENV RAILS_ROOT /app
WORKDIR ${RAILS_ROOT}

RUN mkdir log

COPY public public/
COPY docker/web/nginx.conf /etc/nginx/nginx.conf

EXPOSE 5000

CMD ["nginx", "-g", "daemon off;"]