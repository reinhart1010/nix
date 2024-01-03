---
layout: page
title: linux/dnf (Türkçe)
description: "RHEL, Fedora ve CentOS için paket yönetim aracı (yum'un yerini alır)."
content_hash: 23bcd7901ca65c6a85a3b23272a1591bbc1899ae
last_modified_at: 2024-01-03
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dnf

RHEL, Fedora ve CentOS için paket yönetim aracı (yum'un yerini alır).
Daha fazla bilgi için: <https://dnf.readthedocs.io>.

- Kurulu paketleri kullanılabilir en yeni sürümlere yükselt:

`sudo dnf upgrade`

- Anahtar kelimeler kullanarak paket ara:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anahtar_kelimeler1 anahtar_kelimeler2 ...</span>

- Bir paketin ayrıntılarını göster:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Yeni bir paket kur:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1 paket2 ...</span>

- Bir paketi kaldır:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1 paket2 ...</span>

- Kurulu paketleri listele:

`dnf list --installed`

- Verilen dosyayı hangi paketlerin sağladığını bul:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya</span>
