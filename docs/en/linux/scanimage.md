---
layout: page
title: linux/scanimage (English)
description: "Scan images with the Scanner Access Now Easy API."
content_hash: ac0eb5bc51151885d79563a1bddf3f40def235e8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# scanimage

Scan images with the Scanner Access Now Easy API.
More information: <http://sane-project.org/man/scanimage.1.html>.

- List available scanners to ensure the target device is connected and recognized:

`scanimage -L`

- Scan an image and save it to a file:

`scanimage --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pnm|tiff|png|jpeg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_image</span>
