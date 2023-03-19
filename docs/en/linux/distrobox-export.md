---
layout: page
title: linux/distrobox-export (English)
description: "Export app/service/binary from container to host OS."
content_hash: de606ae5544aa1042f311262e39efcc2713a6715
last_modified_at: 2023-03-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-export

Export app/service/binary from container to host OS.
Subcommand of `distrobox`. See also: `tldr distrobox`.
More information: <https://distrobox.privatedns.org/usage/distrobox-export.html>.

- Export an app from the container to the host (the desktop entry/icon will show up in your host system's application list):

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --extra-flags "--foreground"`

- Export a binary from the container to the host:

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_on_host</span>

- Export a binary from the container to the host (i.e.`$HOME/.local/bin`) :

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/export</span>

- Export a service from the container to the host (`--sudo` will run the service as root inside the container):

`distrobox-export --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --extra-flags "--allow-newer-config" --sudo`

- Unexport/delete an exported application:

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --delete`
