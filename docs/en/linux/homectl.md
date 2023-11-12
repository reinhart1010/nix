---
layout: page
title: linux/homectl (English)
description: "Create, remove, change or inspect home directories using the systemd-homed service."
content_hash: 54ccf5c4f5ece90afbd6eb5c64002c52c8a1030f
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/homectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# homectl

Create, remove, change or inspect home directories using the systemd-homed service.
More information: <https://manned.org/homectl>.

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
