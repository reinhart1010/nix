---
layout: page
title: common/podman-build (English)
description: "Daemonless tool for building container images."
content_hash: 3215b346cc5116035cbb4e230b6cd5529539b2ce
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/podman-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman build

Daemonless tool for building container images.
Podman provides a Docker-CLI comparable command-line. Simply put: `alias docker=podman`.
More information: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Create an image using a `Dockerfile` or `Containerfile` in the specified directory:

`podman build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create an image with a specified tag:

`podman build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name:version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create an image from a non-standard file:

`podman build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Containerfile.different</span>` .`

- Create an image without using any previously cached images:

`podman build --no-cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create an image suppressing all output:

`podman build --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
