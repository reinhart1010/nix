---
layout: page
title: linux/homectl (English)
description: "Create, remove, change or inspect home directories using the systemd-homed service."
content_hash: 7a936e71f1c9c26914fadbbf1567f23abe442687
---
# homectl

Create, remove, change or inspect home directories using the systemd-homed service.
More information: <https://man.archlinux.org/man/homectl.1>.

- List user accounts and their associated home directories:

`homectl list`

- Create a user account and their associated home directory:

`sudo homectl create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a specific user and the associated home directory:

`sudo homectl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Change the password for a specific user:

`sudo homectl passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Run a shell or a command with access to a specific home directory:

`sudo homectl with `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Lock or unlock a specific home directory:

`sudo homectl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lock|unlock</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Change the disk space assigned to a specific home directory to 100 GiB:

`sudo homectl resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100G</span>

- Display help:

`homectl --help`
