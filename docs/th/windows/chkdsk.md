---
layout: page
title: windows/chkdsk (ไทย)
description: "ความสมบูรณ์ของระบบไฟล์และข้อมูลเมตาของระบบไฟล์บนดิสก์โวลุ่มและแก้ไขข้อผิดพลาดของระบบ"
content_hash: e46c56e5c88b29a71266fe27372be7be6a8327f0
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chkdsk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chkdsk

ความสมบูรณ์ของระบบไฟล์และข้อมูลเมตาของระบบไฟล์บนดิสก์โวลุ่มและแก้ไขข้อผิดพลาดของระบบ
ข้อมูลเพิ่มเติม: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- ระบุตัวอักษรไดรฟ์ (ตามด้วยเครื่องหมาย colon), mount point, หรือชื่อของไดรฟ์:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ไดรฟ์</span>

- แก้ไขข้อผิดพลาดของไดรฟ์ที่เลือก:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ไดรฟ์</span>` /f`

- ปิดการใช้งานไดรฟ์ที่เลือกก่อนการตรวจสอบ:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ไดรฟ์</span>` /x`

- เปลี่ยนขนาดของไฟล์ log เป็นไปตามขนาดที่ระบุ (เฉพาะ NTFS):

`chkdsk /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ขนาด</span>
