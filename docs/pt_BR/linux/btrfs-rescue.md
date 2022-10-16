---
layout: page
title: linux/btrfs-rescue (português (Brasil))
description: "Tenta recuperar um sistema de arquivos btrfs danificado."
content_hash: cfecbcde18f6c30d9ab9805a70d300b8ed48bc38
related_topics:
  - title: English version
    url: /en/linux/btrfs-rescue.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs rescue

Tenta recuperar um sistema de arquivos btrfs danificado.
Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-rescue>.

- Reconstrói a árvore de metadados do sistema de arquivos (muito lento):

`sudo btrfs rescue chunk-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Corrige problemas relacionados ao alinhamento do tamanho do dispositivo (por exemplo, incapaz de montar o sistema de arquivos com incompatibilidade de super total de bytes):

`sudo btrfs rescue fix-device-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Recupera um superblock corrompido das cópias corretas (recupere a raiz da árvore do sistema de arquivos):

`sudo btrfs rescue super-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Recupera-se de uma transação interrompida (corrige problemas de repetição de log):

`sudo btrfs rescue zero-log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Cria um dispositivo de controle `/dev/btrfs-control` quando o `mknod` não estiver instalado:

`sudo btrfs rescue create-control-device`
