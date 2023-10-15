---
layout: page
title: common/touch (português (Brasil))
description: "Cria arquivos e define tempo de acesso/modificação."
content_hash: 344375dbeec1ac7905b925bb4d4a179ccce3b11f
last_modified_at: 2023-10-15
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/touch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># touch

Cria arquivos e define tempo de acesso/modificação.
Mais informações: <https://manned.org/man/freebsd-13.1/touch>.

- Cria arquivos especificados:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Define o tempo de [a]cesso ou [m]odificação do arquivo como o atual e não [c]ria o arquivo se ele não existir:

`touch -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Define o [t]empo do arquivo para um valor especificado e não [c]ria o arquivo se ele não existir:

`touch -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Define o tempo de um arquivo específico para o tempo de out[r]o arquivo e não [c]ria o arquivo se ele não existir:

`touch -c -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.emacs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>
