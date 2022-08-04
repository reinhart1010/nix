---
layout: page
title: common/visudo (English)
description: "Safely edit the sudoers file."
content_hash: c8b612fd07410b7e6bcad5c9ec38f3fc6b9a7009
related_topics:
  - title: Nederlands version
    url: /nl/common/visudo.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/visudo.html
    icon: bi bi-globe
---
# visudo

Safely edit the sudoers file.
More information: <https://www.sudo.ws/docs/man/visudo.man>.

- Edit the sudoers file:

`sudo visudo`

- Check the sudoers file for errors:

`sudo visudo -c`

- Edit the sudoers file using a specific editor:

`sudo EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` visudo`

- Display version information:

`visudo --version`
