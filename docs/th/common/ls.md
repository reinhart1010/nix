---
layout: page
title: common/ls (ไทย)
description: "แสดงชื่อ ขนาด หรือข้อมูลเบื้องต้นของแต่ละไฟล์หรือโฟลเดอร์"
content_hash: 04f0a11cce32bf3cb0ac48ba4cda313563ed19cd
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/ls.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ls.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ls

แสดงชื่อ ขนาด หรือข้อมูลเบื้องต้นของแต่ละไฟล์หรือโฟลเดอร์
ข้อมูลเพิ่มเติม: <https://www.gnu.org/software/coreutils/ls>

- แสดงชื่อไฟล์หรือโฟลเดอร์ หนึ่งชื่อต่อบรรทัด:

`ls -1`

- แสดงชื่อไฟล์หรือโฟลเดอร์ทั้งหมด รวมทั้งไฟล์ที่ถูกซ่อนอยู่:

`ls -a`

- แสดงชื่อไฟล์หรือโฟลเดอร์ทั้งหมด โดยที่ชื่อโฟลเดอร์จะมี `/` ตามหลัง:

`ls -F`

- แสดงข้อมูลเบื้องต้นของไฟล์หรือโฟลเดอร์ (สิทธ์การเข้าถึง, ความเป็นเจ้าของ, ขนาด, และวันที่แก้ไขล่าสุด):

`ls -la`

- แสดงข้อมูลเบื้องต้นของไฟล์หรือโฟลเดอร์ (สิทธ์การเข้าถึง, ความเป็นเจ้าของ, ขนาด, และวันที่แก้ไขล่าสุด โดยที่ขนาดจะแสดงผลในหน่วยที่มนุษย์เข้าใจ เช่น KiB, MiB, GiB):

`ls -lh`

- แสดงข้อมูลเบื้องต้นของไฟล์หรือโฟลเดอร์ (สิทธ์การเข้าถึง, ความเป็นเจ้าของ, ขนาด, และวันที่แก้ไขล่าสุด) โดยใช้ขนาดในการเรียงลำดับจากมากไปน้อย:

`ls -lS`

- แสดงข้อมูลเบื้องต้นของไฟล์หรือโฟลเดอร์ (สิทธ์การเข้าถึง, ความเป็นเจ้าของ, ขนาด, และวันที่แก้ไขล่าสุด) โดยใช้วันที่แก้ไขล่าสุดในการเรียงลำดับจากอายุมากไปน้อย:

`ls -ltr`

- แสดงชื่อโฟลเดอร์:

`ls -d */`
