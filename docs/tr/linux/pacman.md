---
layout: page
title: linux/pacman (Türkçe)
description: "Arch Linux paket yönetim aracı."
content_hash: 62f014f483f30c6d02206b57beb1513448786182
last_modified_at: 2024-01-02
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
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Arch Linux paket yönetim aracı.
Ayrıca bakınız: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Tüm paketleri senkronize et ve güncelle:

`sudo pacman -Syu`

- Yeni bir paket indir:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Bir paket ve bağlılıklarını sil:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- İndirilmiş paket ve sürümleri sırala:

`pacman -Q`

- Sadece özellikle belirtilen paket ve sürümleri sırala:

`pacman -Qe`

- Paket çerezlerini boş alan açmak için temizle:

`sudo pacman -Scc`
