---
layout: page
title: linux/konsole (English)
description: "Konsole: The KDE terminal emulator."
content_hash: eb7c5ea7e15da7f4e0a29831ddd9efbbb91c263e
related_topics:
  - title: 中文 version
    url: /zh/linux/konsole.html
    icon: bi bi-globe
---
# konsole

Konsole: The KDE terminal emulator.
More information: <https://konsole.kde.org>.

- Open a new Konsole in a specific directory:

`konsole --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run a specific command and do not close the window after it exits:

`konsole --noclose -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Open a new tab:

`konsole --new-tab`

- Open a Konsole in the background and bring to the front when Ctrl+Shift+F12 (by default) is pressed:

`konsole --background-mode`

- Open a Konsole with the emergency FALLBACK profile:

`konsole --fallback-profile`
