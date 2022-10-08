---
layout: page
title: common/snakefmt (português (Brasil))
description: "Formata arquivos Snakemake."
content_hash: 6e27378a82ba1e9c114e58164fa3f88fc8d6903a
related_topics:
  - title: English version
    url: /en/common/snakefmt.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># snakefmt

Formata arquivos Snakemake.
Mais informações: <https://github.com/snakemake/snakefmt>.

- Formata um Snakefile específico:

`snakefmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/snakefile</span>

- Formata todos os Snakefiles recursivamente em uma pasta específica:

`snakefmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Formata um arquivo usando um arquivo de configuração específico:

`snakefmt --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/config.toml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/snakefile</span>

- Formata um arquivo usando um comprimento máximo de linha específico:

`snakefmt --line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/snakefile</span>

- Exibe às mudanças que seriam realizadas sem realiza-las:

`snakefmt --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/snakefile</span>
