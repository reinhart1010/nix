---
layout: page
title: common/docker-login (English)
description: "Log into a Docker registry."
content_hash: 882a060f3058dc4c3ecb8bbf32f3e56e11b4fe87
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-login.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-login.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker login

Log into a Docker registry.
More information: <https://docs.docker.com/reference/cli/docker/login/>.

- Interactively log into a registry:

`docker login`

- Log into a registry with a specific username (user will be prompted for a password):

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Log into a registry with username and password:

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Log into a registry with password from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password-stdin`
