---
layout: page
title: common/docker-exec (Türkçe)
description: "Halihazırda çalışan bir Docker konteyneri üstünde komut çalıştır."
content_hash: d3b133fe5c0ddd3cab1084219fa6fc6f32668762
last_modified_at: 2023-12-30
related_topics:
  - title: Deutsch version
    url: /de/common/docker-exec.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-exec.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-exec.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-exec.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker exec

Halihazırda çalışan bir Docker konteyneri üstünde komut çalıştır.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Halihazırda çalışan bir konteynerin üstünde interaktif bir kabuk oturumunu çalıştır:

`docker exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Halihazırda çalışan bir konteynerin üstüne arkaplanda çalışmak üzere (ayrılmış) bir komut çalıştır:

`docker exec --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Belirtilen bir komutu üstünde çalıştırmak adına çalışan dizini seç:

`docker exec --interactive --tty --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Varolan konteyner üstünde arkaplanda çalışmak üzere bir komut çalıştır ancak `stdin`'i açık tut:

`docker exec --interactive --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Çalışmakta olan bir bash oturumu içinde bir çevre değişkeni belirle:

`docker exec --interactive --tty --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">değişken_ismi</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Belirtilmiş bir kullanıcı olarak komut çalıştır:

`docker exec --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcı</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>
