---
layout: page
title: linux/toolbox-enter (English)
description: "Enter a `toolbox` container for interactive use."
content_hash: 0703a1974873f1d0ce71ec385854827d88c07e0d
last_modified_at: 2023-11-13
related_topics:
  - title: தமிழ் version
    url: /ta/linux/toolbox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox enter

Enter a `toolbox` container for interactive use.
See also: `toolbox run`.
More information: <https://manned.org/toolbox-enter.1>.

- Enter a `toolbox` container using the default image of a specific distribution:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>

- Enter a `toolbox` container using the default image of a specific release of the current distribution:

`toolbox enter --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>

- Enter a toolbox container using the default image for Fedora 39:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
