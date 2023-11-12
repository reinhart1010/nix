---
layout: page
title: linux/arch-chroot (English)
description: "Enhanced `chroot` command to help in the Arch Linux installation process."
content_hash: 8ffe1f63a6138cce68e4be1d08b5669e90289449
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/arch-chroot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arch-chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arch-chroot

Enhanced `chroot` command to help in the Arch Linux installation process.
More information: <https://man.archlinux.org/man/arch-chroot.8>.

- Start an interactive shell (`bash`, by default) in a new root directory:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new/root</span>

- Specify the user (other than the current user) to run the shell as:

`arch-chroot -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new/root</span>

- Run a custom command (instead of the default `bash`) in the new root directory:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Specify the shell, other than the default `bash` (in this case, the `zsh` package should have been installed in the target system):

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
