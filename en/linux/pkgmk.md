---
layout: page
title: linux/pkgmk (English)
description: "Make a binary package for use with pkgadd on CRUX."
content_hash: ffbd6431e65d5e200f088a32fe804f439dd0f2f9
---
# pkgmk

Make a binary package for use with pkgadd on CRUX.

- Make and download a package:

`pkgmk -d`

- Install the package after making it:

`pkgmk -d -i`

- Upgrade the package after making it:

`pkgmk -d -u`

- Ignore the footprint when making a package:

`pkgmk -d -if`

- Ignore the MD5 sum when making a package:

`pkgmk -d -im`

- Update the package's footprint:

`pkgmk -uf`
