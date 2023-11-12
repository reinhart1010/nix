---
layout: page
title: linux/systemctl (English)
description: "Control the systemd system and service manager."
content_hash: 462e499be14831d34e7f99c95a387de08f5ca6dd
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

Control the systemd system and service manager.
More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Show all running services:

`systemctl status`

- List failed units:

`systemctl --failed`

- Start/Stop/Restart/Reload a service:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- Show the status of a unit:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- Enable/Disable a unit to be started on bootup:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- Mask/Unmask a unit to prevent enablement and manual activation:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- Reload systemd, scanning for new or changed units:

`systemctl daemon-reload`

- Check if a unit is enabled:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>
