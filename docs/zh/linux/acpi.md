---
layout: page
title: linux/acpi (中文)
description: "显示电池状态或热量信息。"
content_hash: 7e7f3def273005a3c0e499ee789b40883ec4e8ec
related_topics:
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
---
# acpi

显示电池状态或热量信息。
更多信息：<https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- 显示电池信息：

`acpi`

- 显示热量（温度）信息：

`acpi -t`

- 显示冷却设备信息：

`acpi -c`

- 用华氏度单位显示热量（温度）信息：

`acpi -tf`

- 显示所有信息：

`acpi -V`

- 从 `/proc` 而非 `/sys` 中提取信息：

`acpi -p`
