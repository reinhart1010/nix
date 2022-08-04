---
layout: page
title: linux/winetricks (English)
description: "Manage Wine virtual Windows environments."
content_hash: e504c2f439cfbac428915f8a32b892e1103dd28d
---
# winetricks

Manage Wine virtual Windows environments.
More information: <https://wiki.winehq.org/Winetricks>.

- Start a graphical setup at the default Wine location:

`winetricks`

- Specify a custom Wine directory to run Winetricks in:

`WINEPREFIX=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wine_directory</span>` winetricks`

- Install a Windows DLL or component to the default Wine directory:

`winetricks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
