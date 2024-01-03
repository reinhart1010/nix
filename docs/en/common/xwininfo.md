---
layout: page
title: common/xwininfo (English)
description: "Display information about windows."
content_hash: ef5c4ccd466c0bc7f8c142c6709f52e82c320094
last_modified_at: 2024-01-03
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/xwininfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xwininfo

Display information about windows.
See also: `xprop`, `xkill`.
More information: <https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>.

- Display a cursor to select a window to display its attributes (id, name, size, position, ...):

`xwininfo`

- Display the tree of all windows:

`xwininfo -tree -root`

- Display the attributes of a window with a specific ID:

`xwininfo -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Display the attributes of a window with a specific name:

`xwininfo -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display the ID of a window searching by name:

`xwininfo -tree -root | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
