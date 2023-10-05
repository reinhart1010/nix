---
layout: page
title: common/identify (English)
description: "Describe the format and characteristics of one or more image files."
content_hash: f87b7ee2cfbadb41a48fa0c6b697018186b26761
last_modified_at: 2023-10-05
---
# identify

Describe the format and characteristics of one or more image files.
Part of ImageMagick.
More information: <https://imagemagick.org/script/identify.php>.

- Describe the format and basic characteristics of an image:

`identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Describe the format and verbose characteristics of an image:

`identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Collect dimensions of all JPEG files in the current directory and save them into a CSV file:

`identify -format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%f,%w,%h\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filelist.csv</span>
