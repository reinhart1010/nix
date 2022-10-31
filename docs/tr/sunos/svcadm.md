---
layout: page
title: sunos/svcadm (Türkçe)
description: "Servisleri idare et."
content_hash: c6f2029e48618d2440dcfd6b201a07c77368051e
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svcadm

Servisleri idare et.
Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Servis veritabanındaki bir servisi etkinleştir:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>

- Servisi devre dışı bırak:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>

- Çalışan bir servisi yeniden başlat:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>

- Servise yapulandırma dosyalarını yeniden okumasını emret:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>

- Bir servisi bakım durumundan çıkar ve başlamasını emret:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>
