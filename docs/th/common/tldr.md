---
layout: page
title: common/tldr (ไทย)
description: "แสดงตัวอย่างแบบง่ายสำหรับเครื่องมือบน command-line จากโปรเจคท์ tldr-pages."
content_hash: 55e3fd68cf79a884e15b78a48f5b75eee8a60935
last_modified_at: 2023-11-22
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr

แสดงตัวอย่างแบบง่ายสำหรับเครื่องมือบน command-line จากโปรเจคท์ tldr-pages.
ข้อมูลเพิ่มเติม: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>

- แสดงตัวอย่างการใช้งานคำสั่งที่ใช้บ่อย (บอกใบ้นิดนึง: นี่คือเหตุผลที่คุณสนใจใช้บริการของเราใช่ไหมล่ะ!):

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- แสดงหน้า tldr ของคำสั่ง tar สำหรับระบบปฏิบัติการ Linux:

`tldr -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar</span>

- ขอความช่วยเหลือการใช้งานคำสั่งย่อยของ Git:

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git-checkout</span>

- ปรับปรุงข้อมูล tldr บนเครื่องของคุณให้ทันสมัย (ถ้าเครื่องของคุณรองรับการ caching):

`tldr -u`
