---
layout: page
title: sunos/truss (Türkçe)
description: "İzleme sistem çağrıları için sorun giderme aracı."
content_hash: 5adced72930a32517f3df15d1bb40883bf9fa746
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/truss.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/sunos/truss.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
tldri18n_status: 2
---
# truss

İzleme sistem çağrıları için sorun giderme aracı.
SunOS'in strace alternatifi.
Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1/truss>.

- Bir programı tüm alt işlemleriyle beraber çalıştırarak başlat:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Belirtilen işlemi onun PID değerini girerek izlemeye başla:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Bir programı argümanları ve çevresel değerlerini göstererek başlar:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Her bir sistem çağrısı için zaman, çağrı ve hataları say ve program çıkışında bunların özetini bildir:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Bir işlemi onun çıktısını sistem çağrısıyla süzerek izle:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_çağrısı_ismi</span>
