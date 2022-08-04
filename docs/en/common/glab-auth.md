---
layout: page
title: common/glab-auth (English)
description: "Authenticate with a GitLab host from the command-line."
content_hash: d811b3b2dbb31bb05380a2edfd0d5ac133513a27
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab auth

Authenticate with a GitLab host from the command-line.
More information: <https://glab.readthedocs.io/en/latest/auth>.

- Log in with interactive prompt:

`glab auth login`

- Log in with a token:

`glab auth login --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Check authentication status:

`glab auth status`

- Log in to a specific GitLab instance:

`glab auth login --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gitlab.example.com</span>
