---
layout: page
title: common/tlmgr-gui (English)
description: "Start a graphical user interface for `tlmgr`."
content_hash: 685507a5853c4f17db011d9b435bcb6baa53e45d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr gui

Start a graphical user interface for `tlmgr`.
`tlmgr gui` depends on the package `perl-tk`, which has to be installed manually.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Start a GUI for `tlmgr`:

`sudo tlmgr gui`

- Start a GUI specifying the background color:

`sudo tlmgr gui -background "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#f39bc3</span>`"`

- Start a GUI specifying the foreground color:

`sudo tlmgr gui -foreground "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#0ef3bd</span>`"`

- Start a GUI specifying the font and font size:

`sudo tlmgr gui -font "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">helvetica 18</span>`"`

- Start a GUI setting a specific geometry:

`sudo tlmgr gui -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpos</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ypos</span>

- Start a GUI passing an arbitrary X resource string:

`sudo tlmgr gui -xrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xresource</span>
