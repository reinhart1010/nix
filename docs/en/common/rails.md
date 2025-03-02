---
layout: page
title: common/rails (English)
description: "A server-side MVC framework written in Ruby."
content_hash: ec3f01812d71d8455a50e829b1b3807429d02151
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/rails.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rails.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rails.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails

A server-side MVC framework written in Ruby.
Some subcommands such as `generate` have their own usage documentation.
More information: <https://guides.rubyonrails.org/command_line.html>.

- Create a new rails project:

`rails new "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>`"`

- Generate a scaffold for a model named Post, predefining the attributes title and body:

`rails generate scaffold Post title:string body:text`

- Run migrations:

`rails db:migrate`

- List all routes:

`rails routes`

- Start local server for current project on port 3000:

`rails server`

- Start local server for current project on a specified port:

`rails server -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`"`

- Open console to interact with application from command-line:

`rails console`

- Check current version of rails:

`rails --version`
