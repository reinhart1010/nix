---
layout: page
title: common/join (português (Brasil))
description: "Junta linhas de dois arquivos ordenados em um campo comum."
content_hash: 1f3fedfb101c5f454690e2a06b9f89dde1814c8b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/join.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/join.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/join.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/join.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># join

Junta linhas de dois arquivos ordenados em um campo comum.
Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

- Junta dois arquivos no primeiro campo (padrão):

`join `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>

- Junta dois arquivos usando uma vírgula (em vez de um espaço) como separador de campo:

`join -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">','</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>

- Junta campo3 do arquivo1 ao campo1 do arquivo2:

`join -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>

- Produz uma linha para cada linha que não pode ser pareada para o arquivo1:

`join -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>
