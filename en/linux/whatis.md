---
layout: page
title: linux/whatis (English)
description: "Display one-line descriptions from manual pages."
content_hash: 55f6e4ea13dfa222db03ed36b1fe9f83998559be
related_topics:
  - title: فارسی version
    url: /fa/linux/whatis.html
    icon: bi bi-globe
---
# whatis

Display one-line descriptions from manual pages.

- Display a description from a man page:

`whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Don't cut the description off at the end of the line:

`whatis --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display descriptions for all commands matching a glob:

`whatis --wildcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net*</span>

- Search man page descriptions with a regular expression:

`whatis --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wish[0-9]\.[0-9]</span>`'`
