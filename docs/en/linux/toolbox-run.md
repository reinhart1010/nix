---
layout: page
title: linux/toolbox-run (English)
description: "Run a command in an existing `toolbox` container."
content_hash: 46a274a8155b31ad71ad6469d6750ddc8f9723c8
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/linux/toolbox-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox run

Run a command in an existing `toolbox` container.
See also: `toolbox enter`.
More information: <https://manned.org/toolbox-run>.

- Run a command inside a specific `toolbox` container:

`toolbox run --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command inside a `toolbox` container for a specific release of a distribution:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run `emacs` inside a `toolbox` container using the default image for Fedora 38:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f38</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>
