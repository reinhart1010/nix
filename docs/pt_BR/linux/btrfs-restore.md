---
layout: page
title: linux/btrfs-restore (português (Brasil))
description: "Tenta salvar arquivos de um sistema de arquivos btrfs danificado."
content_hash: e5757898825d83bc2962e58ea46a873f100cda9a
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs restore

Tenta salvar arquivos de um sistema de arquivos btrfs danificado.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restaura todos os arquivos de um sistema de arquivos btrfs para um determinado diretório:

`sudo btrfs restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_alvo</span>

- Lista (sem escrever) os arquivos a serem restaurados de um sistema de arquivos btrfs:

`sudo btrfs restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_alvo</span>

- Restaura arquivos correspondentes a determinados padrões regex ([c]ase-insensitive) de um sistema de arquivos btrfs (todos os diretórios pai do(s) arquivo(s) de destino também devem corresponder):

`sudo btrfs restore --path-regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_alvo</span>

- Restaura arquivos de um sistema de arquivos btrfs usando um `bytenr` específico da árvore raiz (consulte `btrfs-find-root`):

`sudo btrfs restore -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bytenr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_alvo</span>

- Restaura arquivos de um sistema de arquivos btrfs (juntamente com metadados, atributos estendidos e Symlinks), sobrescrevendo arquivos no destino:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/dispositivo_btrfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_alvo</span>
