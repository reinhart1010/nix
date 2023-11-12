---
layout: page
title: linux/systemd-firstboot (English)
description: "Initialize basic system settings on or before the first boot-up of a system."
content_hash: 0fad4e6ac252fd868142411248f09481744fbd47
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-firstboot

Initialize basic system settings on or before the first boot-up of a system.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-firstboot.html>.

- Operate on the specified directory instead of the root directory of the host system:

`sudo systemd-firstboot --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root_directory</span>

- Set the system keyboard layout:

`sudo systemd-firstboot --keymap=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keymap</span>

- Set the system hostname:

`sudo systemd-firstboot --hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Set the root user's password:

`sudo systemd-firstboot --root-password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Prompt the user interactively for a specific basic setting:

`sudo systemd-firstboot --prompt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setting</span>

- Force writing configuration even if the relevant files already exist:

`sudo systemd-firstboot --force`

- Remove all existing files that are configured by `systemd-firstboot`:

`sudo systemd-firstboot --reset`

- Remove the password of the system's root user:

`sudo systemd-firstboot --delete-root-password`
