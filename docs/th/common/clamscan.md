---
layout: page
title: common/clamscan (ไทย)
description: "โปรแกรมตรวจหาไวรัสบนคอมมานด์ไลน์"
content_hash: 18fab2ccfdfcedbab60b9acbc8b58e11295a4b50
related_topics:
  - title: English version
    url: /en/common/clamscan.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clamscan

โปรแกรมตรวจหาไวรัสบนคอมมานด์ไลน์
ข้อมูลเพิ่มเติม: <https://www.clamav.net>.

- แสกนไฟล์หาช่องโหว่ทางความปลอดภัย:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไฟล์</span>

- แสกนทุกไฟล์ภายใต้ไดเรคทอรีเพื่อหาช่องโหว่ทางความปลอดภัย:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไดเรคทอรี</span>

- แสกนข้อมูลที่ส่งเข้ามายังอินพุทมาตรฐาน:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">คำสั่ง</span>` | clamscan -`

- เลือกไฟล์หรือไดเรคทอรีข้อมูลพื้นฐานของไวรัส:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไฟล์ข้อมูลพื้นฐาน_หรือ_ไดเรคทอรี</span>

- ทำการแสกนบนไดเรคทอรีปัจจุบันแล้วแสดงข้อมูลของไฟล์ที่ติดไวัส:

`clamscan --infected`

- เขียนผลการแสกนไปยังไฟล์ที่ระบุ:

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไฟล์ที่ระบุ}`

- ย้ายไฟล์ที่พบการติดไวรัสไปยังไดเรคทอรีที่ระบุ:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไดเรคทอรีสำหรับการกักกัน</span>

- ลบไฟล์ที่พบการติดไวรัส:

`clamscan --remove yes`
