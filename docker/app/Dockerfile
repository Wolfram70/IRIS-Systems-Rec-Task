
FROM ruby:3.0.5

RUN mkdir /app
WORKDIR /app

RUN apt-get update -qq && apt-get install build-essential

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock

RUN bundle install
RUN bundle exec rails assets:precompile

CMD ["bundle", "exec", "rails", "s", "-p", "3000", "-b", "0.0.0.0"]