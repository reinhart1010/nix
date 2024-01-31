---
layout: page
title: osx/pbcopy (ไทย)
description: "คัดลอกข้อมูลจากอินพุตมาตรฐาน (`stdin`) ไปยังคลิปบอร์ด"
content_hash: dd77ad8f1baa335c556a06b5dfdfb8695dad5d49
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbcopy

คัดลอกข้อมูลจากอินพุตมาตรฐาน (`stdin`) ไปยังคลิปบอร์ด
เทียบได้กับการกดปุ่ม Cmd + C บนแป้นพิมพ์
ข้อมูลเพิ่มเติม: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>

- คัดลอกเนื้อหาในไฟล์ที่กำหนดไปยังคลิปบอร์ด:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ทาง/ไป/ไฟล์</span>

- คัดลอกผลลัพธ์ของคำสั่งไปยังคลิปบอร์ด:

`find . -type t -name "*.png" | pbcopy`
