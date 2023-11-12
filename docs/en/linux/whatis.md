---
layout: page
title: linux/whatis (English)
description: "Display one-line descriptions from manual pages."
content_hash: 8251684a0c5cf5d428bbf482701e272ce9eb00d8
last_modified_at: 2023-11-12
related_topics:
  - title: فارسی version
    url: /fa/linux/whatis.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/whatis.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Display descriptions in a specific language:

`whatis --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
