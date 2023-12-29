---
layout: page
title: windows/chkdsk (ไทย)
description: "ความสมบูรณ์ของระบบไฟล์และข้อมูลเมตาของระบบไฟล์บนดิสก์โวลุ่มและแก้ไขข้อผิดพลาดของระบบ"
content_hash: b89331dc8f340197b2cbb87c8c3d4f9273e38bb9
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chkdsk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/chkdsk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/chkdsk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkdsk

ความสมบูรณ์ของระบบไฟล์และข้อมูลเมตาของระบบไฟล์บนดิสก์โวลุ่มและแก้ไขข้อผิดพลาดของระบบ
ข้อมูลเพิ่มเติม: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>

- ระบุตัวอักษรไดรฟ์ (ตามด้วยเครื่องหมาย colon), mount point, หรือชื่อของไดรฟ์:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ไดรฟ์</span>

- แก้ไขข้อผิดพลาดของไดรฟ์ที่เลือก:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ไดรฟ์</span>` /f`

- ปิดการใช้งานไดรฟ์ที่เลือกก่อนการตรวจสอบ:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ไดรฟ์</span>` /x`

- เปลี่ยนขนาดของไฟล์ log เป็นไปตามขนาดที่ระบุ (เฉพาะ NTFS):

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ขนาด</span>
