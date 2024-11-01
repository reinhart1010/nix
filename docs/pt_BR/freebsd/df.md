---
layout: page
title: freebsd/df (português (Brasil))
description: "Exibe uma visão geral do uso de espaço de disco do sistema de arquivos."
content_hash: 9195ede52a3bdea81064705467bdfa7f2c838b0a
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/freebsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Exibe uma visão geral do uso de espaço de disco do sistema de arquivos.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?df>.

- Exibe todos os sistemas de arquivos e seu uso de disco usando unidades 512-bytes:

`df`

- Usa unidades legíveis para [h]umanos (baseadas em potências de 1024) e exibe um total:

`df -h -c`

- Usa unidades legíveis para [h]umanos (baseadas em potências de 1000):

`df -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-si|H</span>

- Exibe o sistema de arquivos e seu uso do disco contendo o arquivo ou diretório dado:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Inclui estatísticas do número de nós livres e usados incluindo [T]ipos do sistema de arquivos:

`df -iT`

- Usa unidades 1024-bytes ao escrever figuras de espaço:

`df -k`

- Exibe informação em uma maneira [p]ortátil:

`df -P`
