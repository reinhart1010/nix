---
layout: page
title: common/chroot (Türkçe)
description: "Komut veya etkileşimli komut satırını özel kök diziniyle çalıştırır."
content_hash: ab877f46e7cfd5fae623eb6612f04556da3f3849
last_modified_at: 2024-12-12
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chroot.html
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
tldri18n_status: 2
---
# chroot

Komut veya etkileşimli komut satırını özel kök diziniyle çalıştırır.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Komutu yeni kök dizini olarak çalıştır:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni/kok/yolu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Kullanılacak kullanıcı ve grubu (ID veya isim) belirle:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanici:grup</span>
