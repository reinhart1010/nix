---
layout: page
title: common/pm2 (Indonesia)
description: "Manajer proses untuk Node.js."
content_hash: f386b72b39520d7084bb1521f39b4fadf6e0d75e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pm2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pm2

Manajer proses untuk Node.js.
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
