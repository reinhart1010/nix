---
layout: page
title: common/docker-rmi (English)
description: "Remove one or more Docker images."
content_hash: 37fe1ea74d26404dafa59a2082c9a4bca36c2f8b
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
---
# docker rmi

Remove one or more Docker images.
More information: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Show help:

`docker rmi`

- Remove one or more images given their names:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Force remove an image:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Remove an image without deleting untagged parents:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
