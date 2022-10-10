---
layout: page
title: linux/pwd (ไทย)
description: "แสดงชื่อของไดเรกทอรีที่ทำงานอยู่"
content_hash: 20d1b595504e160a0ee6af9f5a0aec5a549aff71
related_topics:
  - title: English version
    url: /en/linux/pwd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pwd

แสดงชื่อของไดเรกทอรีที่ทำงานอยู่
ข้อมูลเพิ่มเติม: <https://www.gnu.org/software/coreutils/pwd>.

- แสดงชื่อของไดเรกทอรีที่ทำงานอยู่:

`pwd`

- แสดงชื่อของไดเรกทอรีที่ทำงานอยู่ โดยไม่รวม symlinks:

`pwd --physical`

- แสดงชื่อของไดเรกทอรีที่ทำงานอยู่ โดยใช้ PWD จาก environment ถึงแม้ว่าจะรวม symlinks:

`pwd --logical`
