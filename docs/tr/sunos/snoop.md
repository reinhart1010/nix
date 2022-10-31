---
layout: page
title: sunos/snoop (Türkçe)
description: "Ağ paketi inceleyici."
content_hash: c1a869a11564626ee8a6a60dafd52935d33a5021
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># snoop

Ağ paketi inceleyici.
SunOS'in tcpdump alternatifi.
Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Belirtilen ağ arayüzünde paketleri yakala:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- Yakalanan paketleri terminalde göstermek yerine bir dosyaya kaydet:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosyaismi</span>

- Belirtilen dosyadan paketlerin ayrıntılı protokol katman özetini görüntüle:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosyaismi</span>

- Host isminden gelen ağ paketlerini yakala ve belirtilen port'a git:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostismi</span>

- İki IP adresi arasında takas edilen ağ paketleriini yakala ve hex değerlerini göster:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_addresi_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_addresi_2</span>
