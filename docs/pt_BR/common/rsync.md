---
layout: page
title: common/rsync (português (Brasil))
description: "Transfira arquivos para ou de um host remote (mas não entre dois hosts remotos), usando SSH por padrão."
content_hash: c44bb254fc7ce2d0a43e417da07422afce383929
last_modified_at: 2023-10-14
related_topics:
  - title: English version
    url: /en/common/rsync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rsync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rsync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rsync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
---
# rsync

Transfira arquivos para ou de um host remote (mas não entre dois hosts remotos), usando SSH por padrão.
para especificar um caminho remoto, use `host:caminho/para/arquivo_ou_diretório`.
Mais informações: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfere um arquivo:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Usa o modo de arquivo (copia recursivamente diretórios, copia links simbólicos sem resolver e preserva permissões, propriedade e tempos de modificação):

`rsync --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Comprime os dados à medida que são enviados ao destino, exibe progresso detalhado e legível, e mantém arquivos parcialmente transferidos se forem interrompidos:

`rsync --compress --verbose --human-readable --partial --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Copia recursivamente diretórios:

`rsync --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Transfere os conteúdos do diretório, mas não o diretório em si:

`rsync --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Copia recursivamente diretórios, usa o modo de arquivamento, resolve links simbólicos e ignora arquivos que são mais recentes no destino:

`rsync --recursive --archive --update --copy-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Transfere um diretório para um host remoto executando o `rsyncd` and exclui arquivos no destino que não existem na origem:

`rsync --recursive --delete rsync://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Transfere um arquivo por SSH usando uma porta diferente da padrão (22) e mostra o progresso global:

`rsync --rsh 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>
