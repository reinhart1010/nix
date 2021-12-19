---
layout: page
title: common/identify (English)
description: "Command-line utility of Image Magick project to describe the format and characteristics of one or more image files."
content_hash: e684e3eb7846b183b202cd8b3f53667aea6fe2f5
---
# identify

Command-line utility of Image Magick project to describe the format and characteristics of one or more image files.
More information: <https://imagemagick.org/script/identify.php>.

- Describe the format and basic characteristics of an image:

`identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Describe the format and verbose characteristics of an image:

`identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Collect dimensions of all JPEG files under current directory:

`identify -format "%f,%w,%h\n" *.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filelist.csv</span>
