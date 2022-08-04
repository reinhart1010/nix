---
layout: page
title: common/doctl-auth (English)
description: "Authenticate doctl with one or more API tokens."
content_hash: 8e4f72d09af0b89e227171340bc01c3c7072c63b
---
# doctl auth

Authenticate doctl with one or more API tokens.
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
