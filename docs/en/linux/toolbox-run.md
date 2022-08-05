---
layout: page
title: linux/toolbox-run (English)
description: "Run a command in an existing `toolbox` container."
content_hash: 4c9b6b1bc8d5956ebfd353b60d0135271cf98d1f
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox run

Run a command in an existing `toolbox` container.
See also: `toolbox enter`.
More information: <https://manned.org/toolbox-run>.

- Run a command inside a specific `toolbox` container:

`toolbox run --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command inside a `toolbox` container for a specific release of a distribution:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run `emacs` inside a `toolbox` container using the default image for Fedora 36:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f36</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>
