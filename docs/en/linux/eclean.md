---
layout: page
title: linux/eclean (English)
description: "Clean repository source files and binary packages."
content_hash: d3472dd67561e8f72639ab44ca35ee71e52ec887
last_modified_at: 2024-12-08
tldri18n_status: 2
---
# eclean

Clean repository source files and binary packages.
More information: <https://wiki.gentoo.org/wiki/Eclean>.

- Clean the source file directory:

`sudo eclean distfiles`

- Clean the binary package directory:

`sudo eclean packages`

- Clean the distfiles of all uninstalled packages, but keep the distfiles of installed packages:

`sudo eclean --deep --package-names distfiles`

- Clean the binary packages of all uninstalled packages, but keep the binaries of installed packages:

`sudo eclean --deep --package-names packages`
