---
layout: page
title: common/chroot (Türkçe)
description: "Komut veya etkileşimli komut satırını özel kök diziniyle çalıştırır."
content_hash: 1bb12e8618c51ddc20aa9e1e69de64eecf8d795c
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chroot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chroot.html
    icon: bi bi-globe
---
# chroot

Komut veya etkileşimli komut satırını özel kök diziniyle çalıştırır.
Daha fazla bilgi: <https://www.gnu.org/software/coreutils/chroot>.

- Komutu yeni kök dizini olarak çalıştır:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni/kok/yolu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Kullanılacak kullanıcı ve grubu (ID veya isim) belirle:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanici:grup</span>
