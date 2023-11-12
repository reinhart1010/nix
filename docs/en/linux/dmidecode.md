---
layout: page
title: linux/dmidecode (English)
description: "Display the DMI (alternatively known as SMBIOS) table contents in a human-readable format."
content_hash: ff3b3f938e3d5082781b45b8695c3c3c7c7b5214
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/dmidecode.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmidecode.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmidecode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmidecode

Display the DMI (alternatively known as SMBIOS) table contents in a human-readable format.
Requires root privileges.
More information: <https://manned.org/dmidecode>.

- Show all DMI table contents:

`sudo dmidecode`

- Show the BIOS version:

`sudo dmidecode -s bios-version`

- Show the system's serial number:

`sudo dmidecode -s system-serial-number`

- Show BIOS information:

`sudo dmidecode -t bios`

- Show CPU information:

`sudo dmidecode -t processor`

- Show memory information:

`sudo dmidecode -t memory`
