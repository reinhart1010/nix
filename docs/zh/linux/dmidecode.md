---
layout: page
title: linux/dmidecode (中文)
description: "以人类可读的格式显示 DMI（也称为 SMBIOS）表内容。"
content_hash: 8557741bb58d46b85c94ac12dbc66e60e29632ca
last_modified_at: 2025-03-02
related_topics:
  - title: català version
    url: /ca/linux/dmidecode.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmidecode.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmidecode.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dmidecode.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmidecode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmidecode

以人类可读的格式显示 DMI（也称为 SMBIOS）表内容。
需要 root 权限。
更多信息：<https://manned.org/dmidecode>.

- 显示所有 DMI 表内容：

`sudo dmidecode`

- 显示 BIOS 版本：

`sudo dmidecode -s bios-version`

- 显示系统的序列号：

`sudo dmidecode -s system-serial-number`

- 显示 BIOS 信息：

`sudo dmidecode -t bios`

- 显示 CPU 信息：

`sudo dmidecode -t processor`

- 显示内存信息：

`sudo dmidecode -t memory`
