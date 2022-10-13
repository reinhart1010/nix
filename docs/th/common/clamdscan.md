---
layout: page
title: common/clamdscan (ไทย)
description: "โปรแกรมแสกนหาไวรัสบนคอมมานด์ไลน์ โดยใช้โปรแกรมพื้นหลัง ClamAV"
content_hash: 3c7c62dd00d9f7547425f34c97d25044523df1ed
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clamdscan

โปรแกรมแสกนหาไวรัสบนคอมมานด์ไลน์ โดยใช้โปรแกรมพื้นหลัง ClamAV
ข้อมูลเพิ่มเติม: <https://www.clamav.net>.

- แสกนข้อบกพร่องของไฟล์หรือไฟล์ในไดเรคทอรี:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไฟล์_หรือ_ไดเรคทอรี่</span>

- แสกนข้อมูลจากสตรีมอินพุทมาตรฐาน:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">คำสั่ง</span>` | clamdscan -`

- แสกนไดเรคทอรีปัจจุบันแล้วแสดงผลไฟล์ที่ตรวจพบความบกพร่อง:

`clamdscan --infected`

- ส่งผลการแสกนไปยังไฟล์ที่ระบุ:

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไฟล์ที่ระบุ</span>

- ย้ายไฟล์ที่พบการติดไวรัสไปยังไดเรคทอรีที่ระบุ:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">หนทาง/ไปยัง/ไดเรคทอรีสำหรับการกักกัน</span>

- ลบไฟล์ที่พบการติดไวรัส:

`clamdscan --remove`

- ใช้มัลติเธรดในการตรวจไดเรคทอรี:

`clamdscan --multiscan`

- ส่งตัวอธิบายไฟล์ไปยังโปรแกรมแสกนพื้นหลังแทนการส่งไฟล์ข้อมูล:

`clamdscan --fdpass`
