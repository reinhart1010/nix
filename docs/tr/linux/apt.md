---
layout: page
title: linux/apt (Türkçe)
description: "Debian tabanlı dağıtımlar için paket yönetim aracı."
content_hash: b257e26321512f466123f932965517696a8b1466
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Debian tabanlı dağıtımlar için paket yönetim aracı.
Ubuntu 16.04 ve sonraki sürümlerde interaktif kullanıldığında `apt-get` için önerilen değiştirme.
Daha fazla bilgi için: <https://manned.org/apt.8>.

- Kullanılabilir paket ve versiyonların listesini yenile (Bu komutu diğer `apt` komutlarından önce kullanmanız önerilir):

`sudo apt update`

- Belirli bir paketi arayın:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Bir paketin bilgilerini gösterin:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Bir paket kurun veya mevcut en son sürüme güncelleyin:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Bir paketi kaldırın (bunun için "purge" kullanmak, yapılandırma dosyalarını da kaldırır):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Kurulu tüm paketleri mevcut en yeni sürümlerine yükseltin:

`sudo apt upgrade`

- Tüm paketleri listeleyin:

`apt list`

- Kurulu paketleri listeleyin:

`apt list --installed`
