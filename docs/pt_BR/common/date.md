---
layout: page
title: common/date (português (Brasil))
description: "Define ou exibe a data do sistema."
content_hash: 1e0b6bde0153d87e0ae65f92d24cbab8b4afd871
last_modified_at: 2023-10-15
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
  - title: Türkçe version
    url: /tr/common/date.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/date.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># date

Define ou exibe a data do sistema.
Mais informações: <https://www.gnu.org/software/coreutils/date>.

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

`date --rfc-3339=s`

- Define a data atual usando o formato `MMDDhhmmYYYY.ss` (`YYYY` e `.ss` são opcionais):

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">093023592021.59</span>

- Exibe o número da semana ISO atual:

`date +%V`
