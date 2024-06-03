---
layout: page
title: common/rsync (português (Brasil))
description: "Transfira arquivos para ou de um host remote (mas não entre dois hosts remotos), usando SSH por padrão."
content_hash: 2bb5944c2fabbb409fb21b620788a1d63d451b15
last_modified_at: 2024-06-03
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
  - title: 한국어 version
    url: /ko/common/rsync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rsync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rsync

Transfira arquivos para ou de um host remote (mas não entre dois hosts remotos), usando SSH por padrão.
Para especificar um caminho remoto, use `host:caminho/para/arquivo_ou_diretório`.
Mais informações: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfere um arquivo:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Usa o modo de arquivo (copia recursivamente diretórios, copia links simbólicos sem resolver e preserva permissões, propriedade e tempos de modificação):

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--archive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Comprime os dados à medida que são enviados ao destino, exibe progresso detalhado e legível, e mantém arquivos parcialmente transferidos se forem interrompidos:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-zvhP|--compress --verbose --human-readable --partial --progress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Copia recursivamente diretórios:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Transfere os conteúdos do diretório, mas não o diretório em si:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Copia diretórios, usa o modo de arquivamento, resolve links simbólicos e ignora arquivos que são mais recentes no destino:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-auL|--archive --update --copy-links</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Transfere um diretório para um host remoto executando o `rsyncd` and exclui arquivos no destino que não existem na origem:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` --delete rsync://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Transfere um arquivo por SSH usando uma porta diferente da padrão (22) e mostra o progresso global:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--rsh</span>` 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>
