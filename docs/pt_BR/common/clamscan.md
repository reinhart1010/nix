---
layout: page
title: common/clamscan (português (Brasil))
description: "Um antivírus de linha de comando."
content_hash: e5a968159de40ff11c236b4e80499b021adce5b0
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/clamscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamscan.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clamscan

Um antivírus de linha de comando.
Mais informações: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Faz uma varredura em um arquivo por vulnerabilidades:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Faz uma varredura em todos os arquivos recursivamente em um diretório específico:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Faz uma varredura nos dados da `stdin` (entrada padrão):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | clamscan -`

- Especifica um arquivo de banco de dados de vírus ou diretório de arquivos:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_ou_arquivo_banco_de_dados</span>

- Faz uma varredura no diretório atual e lista apenas os arquivos infectados:

`clamscan --infected`

- Gera um relatório da varredura para um arquivo de registro:

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_registro</span>

- Move arquivos infectados para um diretório específico:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_de_quarentena</span>

- Remove arquivos infectados:

`clamscan --remove yes`
