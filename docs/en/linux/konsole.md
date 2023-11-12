---
layout: page
title: linux/konsole (English)
description: "KDE's terminal emulator."
content_hash: fafb6157830c18e5238ce7b669db590fc1a6b7e3
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/konsole.html
    icon: bi bi-globe
tldri18n_status: 2
---
# konsole

KDE's terminal emulator.
More information: <https://docs.kde.org/trunk5/en/konsole/konsole/command-line-options.html>.

- Open the terminal in a specific directory:

`konsole --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- [e]xecute a specific command and don't close the window after it exits:

`konsole --noclose -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Open a new tab:

`konsole --new-tab`

- Open the terminal in the background and bring to the front when `Ctrl+Shift+F12` is pressed:

`konsole --background-mode`
