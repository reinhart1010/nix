---
layout: page
title: linux/pacman-mirrors (Türkçe)
description: "Manjaro Linux için pacman aynalistesi oluşturucu."
content_hash: 0920f5857fb3922458e9cfefee355f742309695e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-mirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-mirrors

Manjaro Linux için pacman aynalistesi oluşturucu.
pacman-mirrors'ın çalıştırıldığı her vakit, E`sudo pacman -Syyu` komutu ile veritabanının senkronize edilmesi ve sistemin güncellenmesi gerekir.
Ayrıca bakınız: `pacman`.
Daha fazla bilgi için: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Varsayılan ayarlar ile bir aynalistesi oluştur:

`sudo pacman-mirrors --fasttrack`

- Mevcut aynaların durumunu göster:

`pacman-mirrors --status`

- Mevcut dalı göster:

`pacman-mirrors --get-branch`

- Farklı bir dala geç:

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stabil|instabil|test_ediliyor</span>

- Sadece IP adresinin bulunduğu ülkenin aynalarını kullanarak bir aynalistesi oluştur:

`sudo pacman-mirrors --geoip`
