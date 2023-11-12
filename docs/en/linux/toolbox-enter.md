---
layout: page
title: linux/toolbox-enter (English)
description: "Enter a `toolbox` container for interactive use."
content_hash: 8921a34caf665ae4f4c47379636bd9a28b3da57a
last_modified_at: 2023-11-12
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

- Enter a toolbox container using the default image for Fedora 38:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f38</span>
