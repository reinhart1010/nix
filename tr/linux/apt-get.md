---
layout: page
title: linux/apt-get (Türkçe)
description: "Debian ve Ubuntu paket yönetim aracı."
content_hash: 5849d77b283494204f5138ccdb6e3d07982cf6c5
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
---
# apt-get

Debian ve Ubuntu paket yönetim aracı.
Paket aramak için `apt-cache` komutunu kullanın.
Daha fazla bilgi: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Kullanılabilir paket ve versiyon listesini güncelleyin (diğer `apt-get` komutlarını çalıştırmadan önce kullanmanız önerilir):

`apt-get update`

- Bir paket yükleyin veya son sürüme güncelleyin:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Bir paketi silin:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Bir paketi ve konfigürasyon dosyalarını silin:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Yüklü paketlerin hepsini son sürümlerine yükseltin:

`apt-get upgrade`

- Yerel depoyu temizleyin - kullanılmayan gereksiz paket dosyalarını (.deb) silin:

`apt-get autoclean`

- Artık gerekmeyen paketleri silin:

`apt-get autoremove`

- Yüklenmiş paketleri yükseltin (`upgrade` gibi), ancak gereksiz paketleri silin ve yeni bağımlılıkları memnun edecek ek paketler kurun:

`apt-get dist-upgrade`
