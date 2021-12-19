---
layout: page
title: linux/acpi (English)
description: "Shows battery status or thermal information."
content_hash: 051ce01d351914c307feb9e50b25b9c2360ee46f
related_topics:
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
---
# acpi

Shows battery status or thermal information.
More information: <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- Show battery information:

`acpi`

- Show thermal information:

`acpi -t`

- Show cooling device information:

`acpi -c`

- Show thermal information in Fahrenheit:

`acpi -tf`

- Show all information:

`acpi -V`

- Extract information from `/proc` instead of `/sys`:

`acpi -p`
