---
layout: page
title: common/docker-login (English)
description: "Log into a Docker registry."
content_hash: abfb68935da648028602374121a22fe7fdcbf916
last_modified_at: 2024-03-14
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
More information: <https://docs.docker.com/engine/reference/commandline/login/>.

- Interactively log into a registry:

`docker login`

- Log into a registry with a specific username (user will be prompted for a password):

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Log into a registry with username and password:

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Log into a registry with password from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password-stdin`
