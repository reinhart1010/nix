---
layout: page
title: linux/btrfs-property (português (Brasil))
description: "Obtém, define ou lista propriedades para um determinado objeto de sistema de arquivos btrfs (arquivos, diretórios, subvolumes, sistemas de arquivos ou dispositivos)."
content_hash: 577637619419c79a1a15b4321d78176f72710c2c
related_topics:
  - title: English version
    url: /en/linux/btrfs-property.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs property

Obtém, define ou lista propriedades para um determinado objeto de sistema de arquivos btrfs (arquivos, diretórios, subvolumes, sistemas de arquivos ou dispositivos).
Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-property>.

- Lista as propriedades disponíveis (e descrições) para o objeto btrfs fornecido:

`sudo btrfs property list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/objeto_btrfs</span>

- Obtém todas as propriedades para o objeto btrfs fornecido:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/objeto_btrfs</span>

- Obtém a propriedade `label` (etiqueta) para o sistema de arquivos ou dispositivo btrfs fornecido:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>` label`

- Obtém todas as propriedades específicas do tipo de objeto para o sistema de arquivos ou dispositivo btrfs fornecido:

`sudo btrfs property get -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subvol|filesystem|inode|device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Define a propriedade de `compression` (compactação) para um determinado inode btrfs (um arquivo ou diretório):

`sudo btrfs property set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/inode_btrfs</span>` compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zstd|zlib|lzo|none</span>
