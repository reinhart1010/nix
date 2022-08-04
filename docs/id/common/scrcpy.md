---
layout: page
title: common/scrcpy (Indonesia)
description: "Tampilkan layar and kontrol perangkat Android anda di dalam desktop."
content_hash: 341da6e16637c7526459bf9e858b4d19634d86e9
related_topics:
  - title: English version
    url: /en/common/scrcpy.html
    icon: bi bi-globe
---
# scrcpy

Tampilkan layar and kontrol perangkat Android anda di dalam desktop.
Informasi lebih lanjut: <https://github.com/Genymobile/scrcpy>.

- Tampilkan layar sebuah perangkat yang terhubung:

`scrcpy`

- Tampilkan layar perangkat tertentu berdasarkan ID atau alamat IP-nya (temukan menggunakan perintah `adb devices`):

`scrcpy --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0123456789abcdef|192.168.0.1:5555</span>

- Tampilkan layar dalam mode layar penuh / fullscreen:

`scrcpy --fullscreen`

- Putarkan tampilan layar perangkat dalam kelipatan 90 derajat (berlawanan arah jarum jam):

`scrcpy --rotation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3</span>

- Tunjukkan indikator sentuhan pada perangkat fisik:

`scrcpy --show-touches`

- Rekam tampilan layar perangkat ke dalam file video tertentu:

`scrcpy --record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.mp4</span>

- Tentukan direktori yang akan digunakan untuk memindahkan file (non-APK) ke dalam perangkat melalui drag-and-drop:

`scrcpy --push-target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>
