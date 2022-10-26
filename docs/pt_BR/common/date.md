---
layout: page
title: common/date (português (Brasil))
description: "Define ou exibe a data e horário do sistema."
content_hash: d9bba5b3090224f5bb56fc4e59d9593ccc09f1c2
related_topics:
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

Define ou exibe a data e horário do sistema.
Mais informações: <https://www.gnu.org/software/coreutils/date>.

- Exibe a data atual usando a formatação padrão:

`date +"%c"`

- Exibe a data atual no formato UTC e ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%S%Z"`

- Mostra a data atual em Unix timestamp - segundos desde 00:00:00 UTC de 1 de janeiro de 1970 (Unix epoch):

`date +%s`

- Exibe uma data representada como Unix timestamp utilizando a formatação padrão:

`date -d @1473305798`

- Converte uma data específica pra Unix timestamp:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- Exibe a data atual no formato RFC-3339 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`
