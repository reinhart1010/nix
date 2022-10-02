---
layout: page
title: common/gpgconf (English)
description: "Modify .gnupg home directories."
content_hash: 161f62cb6e7cd9a81e62d261ff866bb2bddeb8bf
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gpgconf

Modify .gnupg home directories.
More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>.

- List all components:

`gpgconf --list-components`

- List the directories used by gpgconf:

`gpgconf --list-dirs`

- List all options of a component:

`gpgconf --list-options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component</span>

- List programs and test whether they are runnable:

`gpgconf --check-programs`

- Reload a component:

`gpgconf --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component</span>
