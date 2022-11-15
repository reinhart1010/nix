---
layout: page
title: linux/btrfs-rescue (português (Brasil))
description: "Tenta recuperar um sistema de arquivos btrfs danificado."
content_hash: 0a4d292df2f097259892811955c96da39e745a0d
related_topics:
  - title: English version
    url: /en/linux/btrfs-rescue.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-rescue.html
    icon: bi bi-globe
---
# btrfs rescue

Tenta recuperar um sistema de arquivos btrfs danificado.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

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
