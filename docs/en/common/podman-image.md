---
layout: page
title: common/podman-image (English)
description: "Manage Docker images."
content_hash: 9045d13edea1a1a7d7a5dfb7c1e4b53d2a8e9c1f
last_modified_at: 2023-03-12
---
# podman image

Manage Docker images.
See also `podman build`, `podman import`, and `podman pull`.
More information: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- List local Docker images:

`podman image ls`

- Delete unused local Docker images:

`podman image prune`

- Delete all unused images (not just those without a tag):

`podman image prune --all`

- Show the history of a local Docker image:

`podman image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
