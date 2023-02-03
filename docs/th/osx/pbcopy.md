---
layout: page
title: osx/pbcopy (ไทย)
description: "คัดลอกข้อมูลจากอินพุตมาตรฐาน (`stdin`) ไปยังคลิปบอร์ด."
content_hash: a3fc16edc3a17c721f9d83462f428212d53366a8
last_modified_at: 2023-02-03
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pbcopy

คัดลอกข้อมูลจากอินพุตมาตรฐาน (`stdin`) ไปยังคลิปบอร์ด.
เทียบได้กับการกดปุ่ม Cmd + C บนแป้นพิมพ์.
ข้อมูลเพิ่มเติม: <https://ss64.com/osx/pbcopy.html>.

- คัดลอกเนื้อหาในไฟล์ที่กำหนดไปยังคลิปบอร์ด:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ทาง/ไป/ไฟล์</span>

- คัดลอกผลลัพธ์ของคำสั่งไปยังคลิปบอร์ด:

`find . -type t -name "*.png" | pbcopy`
