---
layout: page
title: common/pm2 (Indonesia)
description: "Manajer proses untuk Node.js"
content_hash: a5da812c42246355450e0ae97bec8fc65c710f88
related_topics:
  - title: English version
    url: /en/common/pm2.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pm2

Manajer proses untuk Node.js
Digunakan untuk manajemen log, pemantauan, dan pengaturan proses.
Informasi lebih lanjut: <https://pm2.keymetrics.io>.

- Memulai prooses dengan nama yang dapat digunakan untuk operasi selanjutnya:

`pm2 start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>

- Tampilkan daftar proses:

`pm2 list`

- Pantau semua proses:

`pm2 monit`

- Menghentikan sebuah proses:

`pm2 stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>

- Memulai ulang sebuah proses:

`pm2 restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>

- Membuang semua proses dan menghidupkan mereka kembali nanti:

`pm2 save`

- Menghidupkan kembali proses yang sebelumnya dibuang:

`pm2 resurrect`
