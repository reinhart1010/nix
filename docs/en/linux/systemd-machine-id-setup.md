---
layout: page
title: linux/systemd-machine-id-setup (English)
description: "Initialize the machine ID stored in `/etc/machine-id` at install time with a provisioned or randomly generated ID."
content_hash: f86d301db2771457d86489bf9eb47f0b5a8381c0
last_modified_at: 2023-11-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-machine-id-setup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-machine-id-setup

Initialize the machine ID stored in `/etc/machine-id` at install time with a provisioned or randomly generated ID.
Note: Always use `sudo` to execute these commands as they require elevated privileges.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-machine-id-setup.html>.

- Print the generated or committed machine ID:

`systemd-machine-id-setup --print`

- Specify an image policy:

`systemd-machine-id-setup --image-policy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_policy</span>

- Display the output as JSON:

`sudo systemd-machine-id-setup --json=pretty`

- Operate on a disk image instead of a directory tree:

`systemd-machine-id-setup --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/image</span>
