---
layout: page
title: linux/fwupdmgr (English)
description: "A tool for updating device firmware, including UEFI, using `fwupd`."
content_hash: e6461e9c584f55b6dd8a267f115cbe5786a9c209
---
# fwupdmgr

A tool for updating device firmware, including UEFI, using `fwupd`.
More information: <https://fwupd.org/>.

- Display all devices detected by fwupd:

`fwupdmgr get-devices`

- Download the latest firmware metadata from LVFS:

`fwupdmgr refresh`

- List the updates available for devices on your system:

`fwupdmgr get-updates`

- Install firmware updates:

`fwupdmgr update`
