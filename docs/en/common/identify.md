---
layout: page
title: common/identify (English)
description: "Describe the format and characteristics of image files."
content_hash: 5b58740dd676b30738d0ae0376170e9046d43a84
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# identify

Describe the format and characteristics of image files.
Part of ImageMagick.
More information: <https://imagemagick.org/script/identify.php>.

- Describe the format and basic characteristics of an image:

`identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Describe the format and verbose characteristics of an image:

`identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Collect dimensions of all JPEG files in the current directory and save them into a CSV file:

`identify -format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%f,%w,%h\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filelist.csv</span>
