---
layout: page
title: linux/pacman-query (Türkçe)
description: "Arch Linux paket yönetim aracı."
content_hash: c0686552def4d76879b6fdba6532c55fe5595df9
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-query.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --query

Arch Linux paket yönetim aracı.
Ayrıca bakınız: `pacman`.
Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Yüklenmiş paket ve sürümleri sırala:

`pacman --query`

- Sadece özellikle indirilmiş paket ve sürümleri sırala:

`pacman --query --explicit`

- Hangi paketin belirtilen dosyaya sahip olduğunu bul:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_ismi</span>

- İndirilmiş bir pakete dair bilgiyi görüntüle:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Bir paketin içerdiği dosyaları sırala:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Yetim (başka bir pakete bağlılık olarak indirilmiş ancak herhangi bir paket tarafından gerektirilmeyen) paketleri sırala:

`pacman --query --unrequired --deps --quiet`

- Mevcut depolarda bulunmayan, indirilmiş paketleri sırala:

`pacman --query --foreign`

- Miadı dolmuş paketleri sırala:

`pacman --query --upgrades`
