---
layout: page
title: common/middleman (English)
description: "Static site generator written in Ruby."
content_hash: 97d10eec185b9f0420295121aee9bd03f49ebf19
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# middleman

Static site generator written in Ruby.
More information: <https://middlemanapp.com/>.

- Create a new Middleman project:

`middleman init "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>`"`

- Start local server for current project on port 4567:

`middleman server`

- Start local server for current project on a specified port:

`middleman server -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`"`

- Build the project in the current directory to prepare for deployment:

`bundle exec middleman build`

- Deploy the Middleman project in the current directory:

`middleman deploy`
