---
layout: page
title: linux/systemd-nspawn (English)
description: "Spawn a command or OS in a lightweight container."
content_hash: 7b81a3381e54272195eeb7c0083cdddfb6bbb3f4
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# systemd-nspawn

Spawn a command or OS in a lightweight container.
More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- Run a command in a container:

`systemd-nspawn --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/container_root</span>

- Run a full Linux-based OS in a container:

`systemd-nspawn --boot --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/container_root</span>

- Run the specified command as PID 2 in the container (as opposed to PID 1) using a stub init process:

`systemd-nspawn --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/container_root</span>` --as-pid2`

- Specify the machine name and hostname:

`systemd-nspawn --machine=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_host</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/container_root</span>
