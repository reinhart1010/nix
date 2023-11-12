---
layout: page
title: linux/distrobox-enter (English)
description: "Enter a distrobox container. See also: `tldr distrobox`."
content_hash: 18ae26812c396ca74356b0f4e5d33dc4c777f0c5
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-enter

Enter a distrobox container. See also: `tldr distrobox`.
Default command executed is your SHELL, but you can specify different shells or entire commands to execute. If used inside a script, an application, or a service, you can use the `--headless` mode to disable the tty and interactivity.
More information: <https://distrobox.privatedns.org/usage/distrobox-enter.html>.

- Enter a distrobox container:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Enter a distrobox container and run a command at login:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- Enter a distrobox container without instantiating a tty:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
