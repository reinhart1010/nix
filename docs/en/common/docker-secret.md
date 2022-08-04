---
layout: page
title: common/docker-secret (English)
description: "Manage Docker swarm secrets."
content_hash: f89fc162be582fe57aaeae2aba0c7519d7a70e6a
related_topics:
  - title: Deutsch version
    url: /de/common/docker-secret.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-secret.html
    icon: bi bi-globe
---
# docker secret

Manage Docker swarm secrets.
More information: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Create a new secret from stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` -`

- Create a new secret from a file:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List all secrets:

`docker secret ls`

- Display detailed information on one or multiple secrets in a human friendly format:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name1 secret_name2 ...</span>

- Remove one or more secrets:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name1 secret_name2 ...</span>
