---
layout: page
title: linux/pacman (Türkçe)
description: "Arch Linux paket yönetim aracı."
content_hash: 8b4b0bc203b732c55160b99eba1c8301f69b79b9
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Arch Linux paket yönetim aracı.
Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Tüm paketleri senkronize et ve güncelle:

`sudo pacman --sync --refresh --sysupgrade`

- Yeni bir paket indir:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Bir paket ve bağlılıklarını sil:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Paket veritabanını girilen ifade ile arat:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arama_şablonu</span>`"`

- İndirilmiş paket ve sürümleri sırala:

`pacman --query`

- Sadece özellikle belirtilen paket ve sürümleri sırala:

`pacman --query --explicit`

- Hangi paketin belirtilen dosyaya sahip olduğunu bul:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_ismi</span>

- Paket çerezlerini boş alan açmak için temizle:

`sudo pacman --sync --clean --clean`
