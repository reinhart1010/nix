---
layout: page
title: linux/aptitude (Türkçe)
description: "Debian ve Ubuntu paket yönetim aracı."
content_hash: 5e6fc599bd35ae03b71aaf0772ed164697ad1389
related_topics:
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
---
# aptitude

Debian ve Ubuntu paket yönetim aracı.
Daha fazla bilgi: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

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
