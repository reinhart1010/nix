---
layout: page
title: osx/date (Indonesia)
description: "Mengatur atau menampilkan tanggal sistem."
content_hash: 9001d4289f6354d267aea7489e3429fcc4dc23a6
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
---
# date

Mengatur atau menampilkan tanggal sistem.
Informasi lebih lanjut: <https://ss64.com/osx/date.html>.

- Menampilkan tanggal saat ini menggunakan format _locale_:

`date +"%c"`

- Menampilkan tanggal saat ini dalam format UTC and ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Menampilkan tanggal saat ini sebagai _Unix timestamp_ (detik sejak jaman Unix):

`date +%s`

- Menampilkan tanggal tertentu (diwakili sebagai _Unix timestamp_) menggunakan format bawaan:

`date -r 1473305798`
