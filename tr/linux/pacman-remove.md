---
layout: page
title: linux/pacman-remove (Türkçe)
description: "Arch Linux paket yönetim aracı."
content_hash: 9f1e81d36022b7fa335d63aa78f3ead3b2a4ff28
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
---
# pacman --remove

Arch Linux paket yönetim aracı.
Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Bu alt komut için yardım göster:

`pacman --remove --help`

- Bir paket ve bağlılıklarını sil:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Bir paketi ve onun hem bağlılıklarını, hem de konfigürasyon dosyalarını sil:

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Bir paketi telkin olmaksızın sil:

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Yetim (başka bir pakete bağlılık olarak indirilmiş ancak herhangi bir paket tarafından gerektirilmeyen) paketleri sil:

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Bir paketi ve ona bağlı olan tüm öbür paketleri sil:

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- (Bir paketin silinme durumunda) Etkilenecek paketleri (silmeden) listele:

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>
