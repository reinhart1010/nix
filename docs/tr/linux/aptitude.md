---
layout: page
title: linux/aptitude (Türkçe)
description: "Debian ve Ubuntu paket yönetim aracı."
content_hash: 4ef99d8c29828fd9a3dc9b2910ae71393f614b71
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

Debian ve Ubuntu paket yönetim aracı.
Daha fazla bilgi için: <https://manned.org/aptitude.8>.

- Kullanılabilir paket ve sürüm listesini senkronize et. Bu, herhangi bir aptitude komutunu uygulamadan önce çalıştırılmalıdır:

`aptitude update`

- Yeni bir paket ve onun bağımlılıklarını kur:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Paket ara:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- İndirilmiş bir paket ara: (`?installed` bir aptitude arama ifadesidir):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>`)'`

- Bir paket ve onun bağımlılıklarını kaldır:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Yüklü paketleri son kullanılabilir sürümlerine yükselt:

`aptitude upgrade`

- Yüklü paketleri yükle (`aptitude upgrade` gibi), gereksizleri sil ve yeni bağımlılıkları karşılamak üzere ek paketler kur:

`aptitude full-upgrade`

- Bir paketin otomatik yükseltilmesini engellemek için onu beklemede tut:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>`)'`
