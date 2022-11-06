---
layout: page
title: common/cat (Türkçe)
description: "Dosyaları yazdır ve birleştir."
content_hash: fffbf67d267aad2a468ce16f6a5df2665666f252
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cat.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
---
# cat

Dosyaları yazdır ve birleştir.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/cat>.

- Bir dosyanın içeriğini standart çıktıya yazdır:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Birkaç dosyayı bir çıktı dosyasında birleştir:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">çıktı/dosyası/yolu</span>

- Birkaç dosyayı bir çıktı dosyasına ekle:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">çıktı/dosyası/yolu</span>

- Tüm çıkış satırlarını numaralandır:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>

- Yazdırılamayan ve boşluk karakterleri görüntüle (ASCII değilse `M-` önekiyle):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/yolu</span>