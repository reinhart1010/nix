---
layout: page
title: linux/portablectl (English)
description: "A systemd utility for managing and deploying portable service images on Linux systems."
content_hash: 12e7ccfa0ed672f82cd11950e8099f913d90f402
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# portablectl

A systemd utility for managing and deploying portable service images on Linux systems.
More information: <https://www.freedesktop.org/software/systemd/man/portablectl.html>.

- List available portable service images discovered in the portable image search paths:

`portablectl list`

- Attach a portable service image to the host system:

`portablectl attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Detach a portable service image from the host system:

`portablectl detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image|image_name</span>

- Display details and metadata about a specified portable service image:

`portablectl inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Check if a portable service image is attached to the host system:

`portablectl is-attached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image|image_name</span>
