---
layout: page
title: linux/pacman-sync (Türkçe)
description: "Arch Linux paket yönetim aracı."
content_hash: 5de22bbdfc5f941eeb4e3b22642ab73e2a14f405
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
---
# pacman --sync

Arch Linux paket yönetim aracı.
Daha fazla bilgi: <https://man.archlinux.org/man/pacman.8>.

- Yeni bir paket indir::

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Tüm paketleri senkronize et ve güncelle (bahsi geçen paketleri güncellemeden indirmek için `--downloadonly` eki gereklidir)

`sudo pacman --sync --refresh --sysupgrade`

- Tüm paketleri güncelle ve telkin olmaksızın yeni bir tane indir:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Paket veritabanını girilen ifade ile arat:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arama_şablonu</span>`"`

- Bir paket hakkında bilgi görüntüle:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Bir paket güncellemesi sırasında çakışan dosyaların üstüne yaz:

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek_dosya</span>

- Tüm paketleri senkronize et ve güncelle, ancak belli bir paketi yoksay:

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_ismi</span>

- Kullanılmayan paket ve kullanılmamış depoları çerezlerden sil (tüm paketlerin çerezlerini temizlemek için `--clean` eki iki kez kullanılmalıdır):

`sudo pacman --sync --clean`
