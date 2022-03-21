---
layout: page
title: linux/whatis (English)
description: "Display one-line descriptions from manual pages."
content_hash: b733517012f12b56377259cc0352389a4720e505
related_topics:
  - title: فارسی version
    url: /fa/linux/whatis.html
    icon: bi bi-globe
---
# whatis

Display one-line descriptions from manual pages.
More information: <https://manned.org/whatis>.

- Display a description from a man page:

`whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Don't cut the description off at the end of the line:

`whatis --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display descriptions for all commands matching a glob:

`whatis --wildcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net*</span>

- Search man page descriptions with a regular expression:

`whatis --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wish[0-9]\.[0-9]</span>`'`
