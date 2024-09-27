---
layout: page
title: common/docker-pull (English)
description: "Download Docker images from a registry."
content_hash: 2e940167ec8d97237347070fdd75e51e5d90f410
last_modified_at: 2024-09-27
related_topics:
  - title: français version
    url: /fr/common/docker-pull.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker pull

Download Docker images from a registry.
More information: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Download a specific Docker image:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Download a specific Docker image in quiet mode:

`docker pull --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Download all tags of a specific Docker image:

`docker pull --all-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Download a Docker images for a specific platform, e.g. linux/amd64:

`docker pull --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux/amd64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Display help:

`docker pull --help`
