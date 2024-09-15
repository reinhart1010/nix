---
layout: page
title: common/docker-rmi (English)
description: "Remove Docker images."
content_hash: feb34e1dfca7ed2772e6bcef88b0ff8e06f17376
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rmi

Remove Docker images.
More information: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Display help:

`docker rmi`

- Remove one or more images given their names:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Force remove an image:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Remove an image without deleting untagged parents:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
