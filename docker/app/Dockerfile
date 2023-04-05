FROM ruby:3.0.5

RUN mkdir /app
WORKDIR /app

RUN apt-get update -qq && apt-get install build-essential

COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock

RUN bundle install

RUN bundle exec rails assets:precompile
RUN bundle exec rails db:migrate

EXPOSE 8080

CMD ["bundle", "exec", "rails", "s", "-p", "8080", "-b", "0.0.0.0"]