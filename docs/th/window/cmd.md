---
layout: page
title: window/cmd (ไทย)
description: "ตัวแปลคำสั่งของ Windows"
content_hash: ca99b2fd646f8fc85896ee23fef80c8e0874099a
last_modified_at: 2023-07-03
---
# cmd

ตัวแปลคำสั่งของ Windows
ข้อมูลเพิ่มเติม: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd>

- เริ่มเซสชันเชลล์แบบโต้ตอบ:

`cmd`

- รันคำสั่งที่ระบุแล้วปิด ([c]ommand):

`cmd /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>`"`

- ดำเนินการสคริปต์เฉพาะ:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">เส้นทาง\ไปยัง\สคริปต์</span>

- ดำเนินการคำสั่งเฉพาะแล้วป้อนเชลล์แบบโต้ตอบ:

`cmd /k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>`"`

- เริ่มเซสชันเชลล์แบบโต้ตอบโดยที่ 'echo' ถูกปิดใช้งานในเอาต์พุตคำสั่ง:

`cmd /q`

- เริ่มเซสชันเชลล์แบบโต้ตอบโดยเปิดใช้งานหรือปิดใช้งานการขยาย [v]ariable ที่ล่าช้า:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- เริ่มเซสชันเชลล์แบบโต้ตอบด้วยคำสั่ง [e]xtensions ที่เปิดใช้งานหรือปิดใช้งาน:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- บังคับให้เอาต์พุตใช้การเข้ารหัส [u]nicode:

`cmd /u`
