---
layout: page
title: osx/pbcopy (ไทย)
description: "คัดลอกข้อมูลจากอินพุตมาตรฐาน (`stdin`) ไปยังคลิปบอร์ด"
content_hash: 25d2d0019d9ed1e9670e0fc33dd8743554758753
last_modified_at: 2023-07-14
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
# pbcopy

คัดลอกข้อมูลจากอินพุตมาตรฐาน (`stdin`) ไปยังคลิปบอร์ด
เทียบได้กับการกดปุ่ม Cmd + C บนแป้นพิมพ์
ข้อมูลเพิ่มเติม: <https://ss64.com/osx/pbcopy.html>

- คัดลอกเนื้อหาในไฟล์ที่กำหนดไปยังคลิปบอร์ด:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ทาง/ไป/ไฟล์</span>

- คัดลอกผลลัพธ์ของคำสั่งไปยังคลิปบอร์ด:

`find . -type t -name "*.png" | pbcopy`
