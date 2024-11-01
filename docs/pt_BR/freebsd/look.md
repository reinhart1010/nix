---
layout: page
title: freebsd/look (português (Brasil))
description: "Exibe linhas começando com um prefixo em um arquivo ordenado."
content_hash: 3d1e89432be6b8ffb37deabc64df899d8156b784
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/freebsd/look.html
    icon: bi bi-globe
  - title: español version
    url: /es/freebsd/look.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Exibe linhas começando com um prefixo em um arquivo ordenado.
Veja também: `grep`, `sort`.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?look>.

- Busca por linhas começando com um prefixo específico em um arquivo específico:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefixo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Busca sem distinção entre maiúsculas e minúsculas apenas em caracteres alfanuméricos:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefixo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Especifica um caractere de término de string (espaço por padrão):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Busca em `/usr/share/dict/words` (`--ignore-case` e `--alphanum` são assumidos):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefixo</span>
