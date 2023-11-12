---
layout: page
title: common/viu (English)
description: "View images on the terminal."
content_hash: 5dcb5e00e9f153e5d585a84cf362fe09d9b30cde
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# viu

View images on the terminal.
More information: <https://github.com/atanunq/viu>.

- Render an image or animated GIF:

`viu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image or GIF from the internet using `curl`:

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/image.png</span>` | viu -`

- Render an image with a transparent background:

`viu -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image with a specific width and height in pixels:

`viu -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image or GIF and display its file name:

`viu -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
