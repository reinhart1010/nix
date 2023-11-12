---
layout: page
title: common/sudo (English)
description: "Executes a single command as the superuser or another user."
content_hash: 46d0db7b5395698d0b70c407a3f9128941db5927
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/sudo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/sudo.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sudo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sudo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sudo

Executes a single command as the superuser or another user.
More information: <https://www.sudo.ws/sudo.html>.

- Run a command as the superuser:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Edit a file as the superuser with your default editor:

`sudo --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Run a command as another user and/or group:

`sudo --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --group=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- Repeat the last command prefixed with `sudo` (only in `bash`, `zsh`, etc.):

`sudo !!`

- Launch the default shell with superuser privileges and run login-specific files (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Launch the default shell with superuser privileges without changing the environment:

`sudo --shell`

- Launch the default shell as the specified user, loading the user's environment and reading login-specific files (`.profile`, `.bash_profile`, etc.):

`sudo --login --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- List the allowed (and forbidden) commands for the invoking user:

`sudo --list`
