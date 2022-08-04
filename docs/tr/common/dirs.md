---
layout: page
title: common/dirs (Türkçe)
description: "Dizin yığını görüntüler veya üzerinde oynama yapar."
content_hash: 0bf99a9a6cf5e0c1e7207c60051a5dc03ac5ea9c
related_topics:
  - title: Deutsch version
    url: /de/common/dirs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dirs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirs.html
    icon: bi bi-globe
---
# dirs

Dizin yığını görüntüler veya üzerinde oynama yapar.
Dizin yığını, `pushd` ve `popd` komutlarıyla üzerinde oynama yapılabilen, son ziyaret edilen dizinleri gösteren bir listedir.
Daha fazla bilgi: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Dizin yığınını her madde arasında boşluk olacak şekilde görüntüle:

`dirs`

- Dizin yığınını her satır başı tek madde olacak şekilde görüntüle:

`dirs -p`

- Dizin yığınında 0'dan başlamak üzere yalnızca nth girişini göster:

`dirs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Dizin yığınını temizle:

`dirs -c`
