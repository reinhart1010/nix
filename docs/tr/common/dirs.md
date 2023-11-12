---
layout: page
title: common/dirs (Türkçe)
description: "Dizin yığını görüntüler veya üzerinde oynama yapar."
content_hash: 72e5adfab27f07a9a23e9cd6055f2ecc8b0747d9
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# dirs

Dizin yığını görüntüler veya üzerinde oynama yapar.
Dizin yığını, `pushd` ve `popd` komutlarıyla üzerinde oynama yapılabilen, son ziyaret edilen dizinleri gösteren bir listedir.
Daha fazla bilgi için: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Dizin yığınını her madde arasında boşluk olacak şekilde görüntüle:

`dirs`

- Dizin yığınını her satır başı tek madde olacak şekilde görüntüle:

`dirs -p`

- Dizin yığınında 0'dan başlamak üzere yalnızca nth girişini göster:

`dirs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Dizin yığınını temizle:

`dirs -c`
