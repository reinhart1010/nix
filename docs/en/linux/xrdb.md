---
layout: page
title: linux/xrdb (English)
description: "X window server's resource database utility for Unix-like systems."
content_hash: a00ea62b4d7931a6c856e808866b2a9596679f75
last_modified_at: 2023-11-12
related_topics:
  - title: português (Portugal) version
    url: /pt_PT/linux/xrdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xrdb

X window server's resource database utility for Unix-like systems.
More information: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- Start `xrdb` in interactive mode:

`xrdb`

- Load values (e.g. style rules) from a resource file:

`xrdb -load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.Xresources</span>

- Query the resource database and print currently set values:

`xrdb -query`
