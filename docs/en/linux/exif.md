---
layout: page
title: linux/exif (English)
description: "Show and change EXIF information in JPEG files."
content_hash: 63be5e30be751c177a522322b944e45b848309b3
---
# exif

Show and change EXIF information in JPEG files.
More information: <https://github.com/libexif/exif/>.

- Show all recognized EXIF information in an image:

`exif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Show a table listing known EXIF tags and whether each one exists in an image:

`exif --list-tags --no-fixup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>

- Extract the image thumbnail into the file `thumbnail.jpg`:

`exif --extract-thumbnail --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thumbnail.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>

- Show the raw contents of the "Model" tag in the given image:

`exif --ifd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --tag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Model</span>` --machine-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>

- Change the value of the "Artist" tag to John Smith and save to `new.jpg`:

`exif --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.jpg</span>` --ifd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --tag="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Artist</span>`" --set-value="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">John Smith</span>`" --no-fixup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>
