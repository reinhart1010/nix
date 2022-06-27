---
layout: page
title: common/visudo (English)
description: "Safely edit the sudoers file."
content_hash: b18ca8666809be5ebd304f0e4100082cbacb9840
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
More information: <https://www.sudo.ws/man/1.8.13/visudo.man.html>.

- Edit the sudoers file:

`sudo visudo`

- Check the sudoers file for errors:

`sudo visudo -c`

- Edit the sudoers file using a specific editor:

`sudo EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` visudo`

- Display version information:

`visudo --version`
