---
layout: page
title: common/date (português (Brasil))
description: "Define ou exibe a data do sistema."
content_hash: bf9a7e5e38a48b4e3a7d53d6fecbe7938a6fac2d
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/date.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/date.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/date.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

Define ou exibe a data do sistema.
Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- Exibe a data atual usando o formato padrão de localidade:

`date +%c`

- Exibe a data atual em UTC, usando o formato ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Exibe a data atual em Unix timestamp - segundos desde 00:00:00 UTC de 1 de janeiro de 1970 (Unix epoch):

`date +%s`

- Converte uma data especificada como Unix timestamp para o formato padrão:

`date -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>

- Converte uma determinada data pra Unix timestamp:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- Exibe a data atual usando o formato RFC-3339 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339 s`

- Define a data atual usando o formato `MMDDhhmmYYYY.ss` (`YYYY` e `.ss` são opcionais):

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">093023592021.59</span>

- Exibe o número da semana ISO atual:

`date +%V`
