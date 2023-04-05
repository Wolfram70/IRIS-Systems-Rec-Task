FROM ruby:3.0.5

RUN mkdir /app
WORKDIR /app

RUN apt-get update -qq && apt-get install build-essential

COPY . /app/

RUN bundle install