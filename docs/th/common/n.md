---
layout: page
title: common/n (ไทย)
description: "เครื่องมือในการจัดการเวอร์ชั่นของ node."
content_hash: c0c166f11fb55edbe079b5396cac3c5c82f1f372
related_topics:
  - title: English version
    url: /en/common/n.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/n.html
    icon: bi bi-globe
---
# n

เครื่องมือในการจัดการเวอร์ชั่นของ node.
ข้อมูลเพิ่มเติม: <https://github.com/tj/n>.

- ติดตั้ง node เวอร์ชั่นที่กำหนด ถ้าหากเวอร์ชั่นที่กำหนดถูกติดตั้งแล้ว เวอร์ชั่นดังกล่าวจะถูกเปิดใช้งาน:

`n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- แสดงรายชื่อเวอร์ชั่นของ node ที่ถูกติดตั้งไปแล้ว และจะเปิดใช้งานหนึ่งในนั้นเป็นการโต้ตอบ:

`n`

- ลบ node เวอร์ชั่นที่กำหนด:

`n rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- รันไฟล์ที่กำหนด ด้วย node เวอร์ชั่นที่กำหนด:

`n use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.js</span>

- แสดงแสดงชื่อของไดเรกทอรีแบบไบนารี่ของ node เวอร์ชั่นที่กำหนด:

`n bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
