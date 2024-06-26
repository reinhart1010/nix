---
layout: page
title: sunos/prstat (Türkçe)
description: "Aktif işlem istatistiklerini bildir."
content_hash: f87f81dfdbce0814f0526971ef5952ca1008de24
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prstat

Aktif işlem istatistiklerini bildir.
Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/prstat>.

- CPU kullanımına ayrılan tüm işlem ve raporların istatiğini incele:

`prstat`

- Hafıza kullanımına ayrılan tüm işlem ve raporların istatistiğini incele:

`prstat -s rss`

- Her bir kullanıcı için toplam kullanım özetini bildir:

`prstat -t`

- Mikrodurum işlem hesap açıklama bilgisini bildir:

`prstat -m`

- Saniye başı en çok CPU kullanan 5 işlemin listesini yazdır:

`prstat -c -n 5 -s cpu 1`
