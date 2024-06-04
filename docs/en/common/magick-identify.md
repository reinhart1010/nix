---
layout: page
title: common/magick-identify (English)
description: "Describe the format and characteristics of image files."
content_hash: 7c24dc1eeaf55fdb24762727d4cda196b46396a3
last_modified_at: 2024-06-04
tldri18n_status: 2
---
# magick identify

Describe the format and characteristics of image files.
See also: `magick`.
More information: <https://imagemagick.org/script/identify.php>.

- Describe the format and basic characteristics of an image:

`magick identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Describe the format and verbose characteristics of an image:

`magick identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Collect dimensions of all JPEG files in the current directory and save them into a CSV file:

`magick identify -format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%f,%w,%h\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filelist.csv</span>
