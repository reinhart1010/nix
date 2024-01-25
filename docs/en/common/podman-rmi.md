---
layout: page
title: common/podman-rmi (English)
description: "Remove Podman images."
content_hash: 661a4d52264ed7a317fc88f2d8ad1fa2718c6ecb
last_modified_at: 2024-01-25
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/podman-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman rmi

Remove Podman images.
More information: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Remove one or more images given their names:

`podman rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Force remove an image:

`podman rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Remove an image without deleting untagged parents:

`podman rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Display help:

`podman rmi`
