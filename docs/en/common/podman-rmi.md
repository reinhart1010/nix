---
layout: page
title: common/podman-rmi (English)
description: "Remove one or more Podman images."
content_hash: e9ecc5280efccb09d1b460171f00c493995df337
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/podman-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman rmi

Remove one or more Podman images.
More information: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Remove one or more images given their names:

`podman rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Force remove an image:

`podman rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Remove an image without deleting untagged parents:

`podman rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Display help:

`podman rmi`
