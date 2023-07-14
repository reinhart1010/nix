---
layout: page
title: linux/ac (ไทย)
description: "แสดงสถิติที่ผู้ใช้งานได้เชื่อมต่อเข้ามาในระบบเป็นเวลานานเท่าไหร่"
content_hash: 6e459392bc6965836a2380ef0d1d374229ea61c0
last_modified_at: 2023-07-14
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
---
# ac

แสดงสถิติที่ผู้ใช้งานได้เชื่อมต่อเข้ามาในระบบเป็นเวลานานเท่าไหร่
ข้อมูลเพิ่มเติม: <https://www.gnu.org/software/acct/manual/accounting.html#ac>

- แสดงสถิติเวลาที่ผู้ใช้ปัจจุบันได้เชื่อมต่อเข้ามาในระบบในหลักชั่วโมง:

`ac`

- แสดงสถิติเวลาที่ผู้ใช้ทุกคนได้เชื่อมต่อเข้ามาในระบบในหลักชั่วโมง แจกแจงตามผู้ใช้แต่ละคน:

`ac --individual-totals`

- แสดงสถิติเวลาของผู้ใช้ที่ระบุไว้ได้เชื่อมต่อเข้ามาในระบบในหลักชั่วโมง:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ชื่อผู้เข้าใช้</span>

- แสดงสถิติว่าผู้ใช้ที่ระบุไว้ ได้เชื่อมต่อเข้ามาในรบบเป็นเวลากี่ชั่วโมงต่อวัน (พร้อมทั้งแสดงเวลาทั้งหมด):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ชื่อผู้เข้าใช้</span>

- แสดงข้อมูลเพิ่มเติมต่างๆ:

`ac --compatibility`
