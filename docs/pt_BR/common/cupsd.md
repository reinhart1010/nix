---
layout: page
title: common/cupsd (português (Brasil))
description: "Daemon de servidor para o servidor de impressão CUPS."
content_hash: b8cc7ea526ef9258133380d045635953001d1c27
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/cupsd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cupsd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsd

Daemon de servidor para o servidor de impressão CUPS.
Mais informações: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Inicia o `cupsd` em segundo plano, ou seja, como um daemon:

`cupsd`

- Inicia o `cupsd` em primeiro plano:

`cupsd -f`

- Inicia o `cupsd` sob demanda (usado comumente pelo `launchd` ou `systemd`):

`cupsd -l`

- Inicia o `cupsd` usando o arquivo de configuração [`c`]`upsd.conf`:

`cupsd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/cupsd.conf</span>

- Inicia o `cupsd` usando os arquivos de configuração no arquivo `cups-file`[`s`]`.conf`:

`cupsd -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivos-cups.conf</span>

- [t]esta o arquivo de configuração [`c`]`upsd.conf` por erros:

`cupsd -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/cupsd.conf</span>

- [t]esta os arquivos de configuração no arquivo `cups-file`[`s`]`.conf` por erros:

`cupsd -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivos-cups.conf</span>

- Mostra todas as opções disponíveis:

`cupsd -h`
