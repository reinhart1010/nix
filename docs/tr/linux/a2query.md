---
layout: page
title: linux/a2query (Türkçe)
description: "Apache ve Debian tabanlı işletim sistemlerinde çalışma süresi yapılandırmasını kurtar."
content_hash: 5795b802d83777c925397294b50161b3eb322d53
last_modified_at: 2022-12-29
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Apache ve Debian tabanlı işletim sistemlerinde çalışma süresi yapılandırmasını kurtar.
Daha fazla bilgi için: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Etkinleştirilmiş Apache modüllerini sırala:

`sudo a2query -m`

- Belirtilen modülün indirilip indirilmediğini kontrol et:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modül_ismi</span>

- Etkinleştirilmiş sanal hostları sırala:

`sudo a2query -s`

- Mevcut etkinleştirilmiş Çoklu İşlem Modülü'nü görüntüle:

`sudo a2query -M`

- Apache sürümünü görüntüle:

`sudo a2query -v`
