---
layout: page
title: linux/wine (English)
description: "Run Windows programs on Unix."
content_hash: 8a211bba2f3266710cbd98843661b58fdba54dfb
---
# wine

Run Windows programs on Unix.
More information: <https://wiki.winehq.org/>.

- Run `ipconfig.exe` program:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipconfig</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/all</span>

- Run `cmd.exe` in background:

`wine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmd</span>

- Run Windows-like Package Manager:

`wine uninstaller`

- Install MSI packages:

`wine msiexec /i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
