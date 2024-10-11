---
layout: page
title: common/clamdscan (português (Brasil))
description: "Faz uma varredura em busca de vírus usando o ClamAV Daemon."
content_hash: e7d455fadd0e894ecebef3d19b9ee8945e54a870
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamdscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamdscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamdscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamdscan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clamdscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clamdscan

Faz uma varredura em busca de vírus usando o ClamAV Daemon.
Mais informações: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Faz uma varredura em um arquivo ou diretório por vulnerabilidades:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Faz uma varredura nos dados da `stdin` (entrada padrão):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | clamdscan -`

- Faz uma varredura no diretório atual e lista apenas os arquivos infectados:

`clamdscan --infected`

- Gera um relatório da varredura para um arquivo de registro:

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_registro</span>

- Move arquivos infectados para um diretório específico:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_de_quarentena</span>

- Remove arquivos infectados:

`clamdscan --remove`

- Usa várias threads para para fazer uma varredura em um diretório:

`clamdscan --multiscan`

- Passa o descritor de arquivo em vez de transmitir o arquivo para o daemon:

`clamdscan --fdpass`
