---
layout: page
title: linux/imgp (English)
description: "Command-line image resizer and rotator for JPEG and PNG images."
content_hash: 69c26ca365a77f299245bf7b1efb84c7e44b6f0d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# imgp

Command-line image resizer and rotator for JPEG and PNG images.
More information: <https://github.com/jarun/imgp>.

- Convert single images and/or whole directories containing valid image formats:

`imgp -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1366x1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Scale an image by 75% and overwrite the source image to a target resolution:

`imgp -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Rotate an image clockwise by 90 degrees:

`imgp -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
