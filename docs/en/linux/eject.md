---
layout: page
title: linux/eject (English)
description: "Eject cds, floppy disks and tape drives."
content_hash: 7ecad74398936d16fc0d97adb0cb15fddd018f83
---
# eject

Eject cds, floppy disks and tape drives.
More information: <https://manned.org/eject>.

- Display the default device:

`eject -d`

- Eject the default device:

`eject`

- Eject a specific device (the default order is cd-rom, scsi, floppy and tape):

`eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Toggle whether a device's tray is open or closed:

`eject -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Eject a cd drive:

`eject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Eject a floppy drive:

`eject -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/floppy</span>

- Eject a tape drive:

`eject -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/tape</span>
