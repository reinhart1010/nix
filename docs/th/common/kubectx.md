---
layout: page
title: common/kubectx (ไทย)
description: "คำสั่งอรรถประโยชน์สำหรับสลับบริบทของคำสั่ง `kubectl`."
content_hash: 7212239dc2c7b676251e8ad3bd61d63c382de05a
related_topics:
  - title: English version
    url: /en/common/kubectx.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubectx

คำสั่งอรรถประโยชน์สำหรับสลับบริบทของคำสั่ง `kubectl`.
ข้อมูลเพิ่มเติม: <https://github.com/ahmetb/kubectx>.

- แสดงบริบททั้งหมด:

`kubectx`

- สลับบริบทที่กำลังใช้งาน:

`kubectx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ชื่อบริบท</span>

- สลับไปบริบทที่ใช้งานก่อนหน้า:

`kubectx -`

- ลบบริบท:

`kubectx -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ชื่อบริบท</span>
