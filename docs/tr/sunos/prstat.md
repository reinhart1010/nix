---
layout: page
title: sunos/prstat (Türkçe)
description: "Aktif işlem istatistiklerini bildir."
content_hash: f87f81dfdbce0814f0526971ef5952ca1008de24
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prstat

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
