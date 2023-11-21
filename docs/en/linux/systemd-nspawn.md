---
layout: page
title: linux/systemd-nspawn (English)
description: "Spawn a command or OS in a lightweight container."
content_hash: 7b81a3381e54272195eeb7c0083cdddfb6bbb3f4
last_modified_at: 2023-11-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-nspawn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-nspawn

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
