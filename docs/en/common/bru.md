---
layout: page
title: common/bru (English)
description: "CLI for Bruno, an Opensource IDE for exploring and testing APIs."
content_hash: 1b2f5fec5fe0cb77ab7cd926171f59257358d098
last_modified_at: 2024-05-23
related_topics:
  - title: español version
    url: /es/common/bru.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bru

CLI for Bruno, an Opensource IDE for exploring and testing APIs.
More information: <https://docs.usebruno.com/bru-cli/overview>.

- Run all request files from the current directory:

`bru run`

- Run a single request from the current directory by specifying its filename:

`bru run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.bru</span>

- Run requests using an environment:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- Run requests using an environment with a variable:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` --env-var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_value</span>

- Run request and collect the results in an output file:

`bru run --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.json</span>

- Display help:

`bru run --help`
