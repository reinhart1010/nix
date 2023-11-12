---
layout: page
title: sunos/dmesg (Türkçe)
description: "Kernel mesajlarını görüntüle."
content_hash: a6266dd54816e29d80f2f1079fbbd566ecf7445d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Kernel mesajlarını görüntüle.
Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Kernel mesajlarını görüntüle:

`dmesg`

- Sistemde ne kadar fiziksel hafıza kaldığını göster:

`dmesg | grep -i memory`

- Kernel mesajlarını terminal ekranına sığacak ve her satıra bir tane gelecek şekilde göster:

`dmesg | less`
