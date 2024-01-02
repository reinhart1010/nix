---
layout: page
title: sunos/prstat (Türkçe)
description: "Aktif işlem istatistiklerini bildir."
content_hash: 1bab3833aed67ac6e50869d28b6b8ad1b8e2f6b0
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
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

`prstat -c -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -s cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
