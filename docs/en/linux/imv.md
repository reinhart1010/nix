---
layout: page
title: linux/imv (English)
description: "CLI image viewer for wayland and X11 aimed at tiling window managers."
content_hash: 580a3b8bbfd8cf976d8cdcc1ff30af5c039d6663
last_modified_at: 2024-12-01
tldri18n_status: 2
---
# imv

CLI image viewer for wayland and X11 aimed at tiling window managers.
Handles multiple formats including Photoshop (PSD).
More information: <https://sr.ht/~exec64/imv>.

- View multiple images:

`imv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.ext path/to/image2.ext ...</span>

- View in fullscreen mode:

`imv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>

- View images [r]ecursively from a path:

`imv -r --slideshow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/path</span>

- Open multiple images via `stdin`:

`find . -type f -name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.svg</span>`" | imv`

- Make a slideshow from a directory showing each image for 10 seconds:

`imv -t 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- View multiple images from the web:

`curl -Osw '%{filename_effective}\n' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.example.com/[1-10].jpg</span>`' | imv`
