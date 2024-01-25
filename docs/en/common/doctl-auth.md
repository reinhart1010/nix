---
layout: page
title: common/doctl-auth (English)
description: "Authenticate `doctl` with API tokens."
content_hash: 9cd54274f1885067eeff13ff5360c4c5999c79d6
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# doctl auth

Authenticate `doctl` with API tokens.
More information: <https://docs.digitalocean.com/reference/doctl/reference/auth/>.

- Open a prompt to enter an API token and label its context:

`doctl auth init --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_label</span>

- List authentication contexts (API tokens):

`doctl auth list`

- Switch contexts (API tokens):

`doctl auth switch --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_label</span>

- Remove a stored authentication context (API token):

`doctl auth remove --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token_label</span>

- Show available commands:

`doctl auth --help`
