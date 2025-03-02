---
layout: page
title: common/rails-server (English)
description: "Serve the Rails app in the current directory using the Puma web server, which comes bundled with Rails."
content_hash: 9a07e345b9898c5c37b8a4fe895f89a7728182a3
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/rails-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails server

Serve the Rails app in the current directory using the Puma web server, which comes bundled with Rails.
More information: <https://guides.rubyonrails.org/command_line.html#bin-rails-server>.

- Run the web server:

`rails server`

- Run the web server on a specified port:

`rails server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Run the web server on a specified IP address:

`rails server --binding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Run the web server on a specified environment:

`rails server --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>

- Display help:

`rails server --help`
