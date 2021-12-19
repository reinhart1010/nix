---
layout: page
title: linux/pacman-query (Türkçe)
description: "Arch Linux paket yönetim aracı."
content_hash: 79d063a70cb9c6c3608524c98faa8909a9159e84
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
---
# pacman --query

Arch Linux paket yönetim aracı.
Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

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
