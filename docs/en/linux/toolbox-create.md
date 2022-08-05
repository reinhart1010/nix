---
layout: page
title: linux/toolbox-create (English)
description: "Create a new `toolbox` container."
content_hash: 0057cd964bd524345074ed622ec4bdb260ecb30d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox create

Create a new `toolbox` container.
More information: <https://manned.org/toolbox-create.1>.

- Create a `toolbox` container for a specific distribution:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>

- Create a `toolbox` container for a specific release of the current distribution:

`toolbox create --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>

- Create a `toolbox` container with a custom image:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Create a `toolbox` container from a custom Fedora image:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.fedoraproject.org/fedora-toolbox:36</span>

- Create a `toolbox` container using the default image for Fedora 36:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f36</span>
