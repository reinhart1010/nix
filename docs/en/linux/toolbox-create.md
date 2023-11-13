---
layout: page
title: linux/toolbox-create (English)
description: "Create a new `toolbox` container."
content_hash: de748be07887e162695085c698896a2ac54c0139
last_modified_at: 2023-11-13
related_topics:
  - title: தமிழ் version
    url: /ta/linux/toolbox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox create

Create a new `toolbox` container.
More information: <https://manned.org/toolbox-create.1>.

- Create a `toolbox` container for a specific distribution:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>

- Create a `toolbox` container for a specific release of the current distribution:

`toolbox create --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>

- Create a `toolbox` container with a custom image:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Create a `toolbox` container from a custom Fedora image:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.fedoraproject.org/fedora-toolbox:39</span>

- Create a `toolbox` container using the default image for Fedora 39:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
