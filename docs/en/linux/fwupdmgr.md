---
layout: page
title: linux/fwupdmgr (English)
description: "Update device firmware, including UEFI, using `fwupd`."
content_hash: c55e5d56983bb847eb227fd1343b44762753bf40
last_modified_at: 2024-02-25
related_topics:
  - title: தமிழ் version
    url: /ta/linux/fwupdmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fwupdmgr

Update device firmware, including UEFI, using `fwupd`.
More information: <https://fwupd.org/>.

- Display all devices detected by fwupd:

`fwupdmgr get-devices`

- Download the latest firmware metadata from LVFS:

`fwupdmgr refresh`

- List the updates available for devices on your system:

`fwupdmgr get-updates`

- Install firmware updates:

`fwupdmgr update`
