---
layout: page
title: common/docker-run (Türkçe)
description: "Yeni bir Docker konteynerinde bir komut çalıştır."
content_hash: c8dd94219dd92cedbc2ea1da07b055e89079e5d1
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-run.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-run.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-run.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-run.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-run.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-run.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker run

Yeni bir Docker konteynerinde bir komut çalıştır.
Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Yeni bir konteynerde, etiketlenmiş bir imgeden komut çalıştır:

`docker run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge:etiket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Yeni bir konteynerde arkaplanda çalışacak şekilde komut çalıştır ve ID'sini göster:

`docker run --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- İnteraktif mod ve pseudo-TTY'deki bir açık-kapalı konteynerde komut çalıştır:

`docker run --rm --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Yeni bir konteynerde geçebilmiş çevresel değişkenler ile komut çalıştır:

`docker run --env '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">değişken</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">değer</span>`' --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">değişken</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Yeni bir konteynerde bağlama takılı hacimlerle komut çalıştır:

`docker run --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konteyner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Yayınlanmış portları içeren yeni bir konteynerde komut çalıştır:

`docker run --publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_portu</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_portu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>
