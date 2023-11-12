---
layout: page
title: linux/toolbox-create (English)
description: "Create a new `toolbox` container."
content_hash: 799858215772e3933b94f6719d625dd8ac6ec88b
last_modified_at: 2023-11-12
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

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.fedoraproject.org/fedora-toolbox:38</span>

- Create a `toolbox` container using the default image for Fedora 38:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f38</span>
