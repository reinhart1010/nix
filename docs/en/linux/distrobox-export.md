---
layout: page
title: linux/distrobox-export (English)
description: "Export app/service/binary from container to host OS. See also: `tldr distrobox`."
content_hash: abbcead2a62a521afe2de44ba37d91e8945e27b5
last_modified_at: 2023-11-26
related_topics:
  - title: Nederlands version
    url: /nl/linux/distrobox-export.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-export

Export app/service/binary from container to host OS. See also: `tldr distrobox`.
More information: <https://distrobox.it/usage/distrobox-export>.

- Export an app from the container to the host (the desktop entry/icon will show up in your host system's application list):

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --extra-flags "--foreground"`

- Export a binary from the container to the host:

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary_on_host</span>

- Export a binary from the container to the host (i.e.`$HOME/.local/bin`) :

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/export</span>

- Export a service from the container to the host (`--sudo` will run the service as root inside the container):

`distrobox-export --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --extra-flags "--allow-newer-config" --sudo`

- Unexport/delete an exported application:

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --delete`
