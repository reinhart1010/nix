---
layout: page
title: common/podman-image (English)
description: "Manage Docker images."
content_hash: 69625f31884b26d5e0456739e6baaf701b05a38c
last_modified_at: 2023-11-23
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/podman-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman image

Manage Docker images.
See also: `podman build`, `podman import`, and `podman pull`.
More information: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- List local Docker images:

`podman image ls`

- Delete unused local Docker images:

`podman image prune`

- Delete all unused images (not just those without a tag):

`podman image prune --all`

- Show the history of a local Docker image:

`podman image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
