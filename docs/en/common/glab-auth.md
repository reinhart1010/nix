---
layout: page
title: common/glab-auth (English)
description: "Authenticate with a GitLab host."
content_hash: 3cc6eb47b5233eb4bcc047d7ef983f753c89cf82
last_modified_at: 2023-07-16
---
# glab auth

Authenticate with a GitLab host.
More information: <https://glab.readthedocs.io/en/latest/auth>.

- Log in with interactive prompt:

`glab auth login`

- Log in with a token:

`glab auth login --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Check authentication status:

`glab auth status`

- Log in to a specific GitLab instance:

`glab auth login --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gitlab.example.com</span>
