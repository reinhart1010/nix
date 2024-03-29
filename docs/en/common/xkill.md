---
layout: page
title: common/xkill (English)
description: "Kill a window interactively in a graphical session."
content_hash: bff6f1ac9f4e209e8161aefef5745a3b468b8579
last_modified_at: 2024-03-14
related_topics:
  - title: español version
    url: /es/common/xkill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/xkill.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/xkill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xkill.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/xkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xkill

Kill a window interactively in a graphical session.
See also: `kill`, `killall`.
More information: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- Display a cursor to kill a window when pressing the left mouse button (press any other mouse button to cancel):

`xkill`

- Display a cursor to select a window to kill by pressing any mouse button:

`xkill -button any`

- Kill a window with a specific ID (use `xwininfo` to get info about windows):

`xkill -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
