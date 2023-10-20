---
layout: page
title: windows/cmd (ไทย)
description: "ตัวแปลคำสั่งของ Windows"
content_hash: ca99b2fd646f8fc85896ee23fef80c8e0874099a
last_modified_at: 2023-10-20
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmd

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
