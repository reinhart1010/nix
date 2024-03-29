---
layout: page
title: common/clamdscan (ไทย)
description: "โปรแกรมแสกนหาไวรัสบนคอมมานด์ไลน์ โดยใช้โปรแกรมพื้นหลัง ClamAV"
content_hash: 16fb90fba5ee5b13185e8a0c74270678850c89c6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamdscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clamdscan

โปรแกรมแสกนหาไวรัสบนคอมมานด์ไลน์ โดยใช้โปรแกรมพื้นหลัง ClamAV
ข้อมูลเพิ่มเติม: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>

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
