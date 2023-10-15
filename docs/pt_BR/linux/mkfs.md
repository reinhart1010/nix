---
layout: page
title: linux/mkfs (português (Brasil))
description: "Cria um sistema de arquivos Linux em uma partição do disco rígido."
content_hash: 5b42987a852f43792f8591a0b7a1156887c5740f
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/mkfs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfs

Cria um sistema de arquivos Linux em uma partição do disco rígido.
Esse comando está obsoleto em favor dos utilitários mkfs.<tipo> específicos de sistema de arquivos.
Mais informações: <https://manned.org/mkfs>.

- Cria um sistema de arquivo ext2 do Linux em uma partição:

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Cria um sistema de arquivos de um tipo especificado:

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Cria um sistema de arquivos de um tipo especificado e verifica por blocos ruins:

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>
