---
layout: page
title: linux/toolbox-enter (English)
description: "Enter a `toolbox` container for interactive use."
content_hash: d31f09eeab73bb2000f4841f40d00c397fe38913
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox enter

Enter a `toolbox` container for interactive use.
See also: `toolbox run`.
More information: <https://manned.org/toolbox-enter.1>.

- Enter a `toolbox` container using the default image of a specific distribution:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>

- Enter a `toolbox` container using the default image of a specific release of the current distribution:

`toolbox enter --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>

- Enter a toolbox container using the default image for Fedora 36:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f36</span>
