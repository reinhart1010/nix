---
layout: page
title: linux/pkgmk (English)
description: "Make a binary package for use with pkgadd on CRUX."
content_hash: fde01d7f2db54cc95d9daf14ea93cd7ef2c5fa64
last_modified_at: 2023-06-04
---
# pkgmk

Make a binary package for use with pkgadd on CRUX.
More information: <https://docs.oracle.com/cd/E88353_01/html/E37839/pkgmk-1.html>.

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
