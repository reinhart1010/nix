---
layout: page
title: common/rails-db (English)
description: "Various database-related subcommands for Ruby on Rails."
content_hash: c90032b6ba5215ca56259398639c220c0c269a7a
last_modified_at: 2024-11-04
related_topics:
  - title: Indonesia version
    url: /id/common/rails-db.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails db

Various database-related subcommands for Ruby on Rails.
More information: <https://guides.rubyonrails.org/active_record_migrations.html>.

- Create databases, load the schema, and initialize with seed data:

`rails db:setup`

- Access the database console:

`rails db`

- Create the databases defined in the current environment:

`rails db:create`

- Destroy the databases defined in the current environment:

`rails db:drop`

- Run pending migrations:

`rails db:migrate`

- View the status of each migration file:

`rails db:migrate:status`

- Rollback the last migration:

`rails db:rollback`

- Fill the current database with data defined in `db/seeds.rb`:

`rails db:seed`
