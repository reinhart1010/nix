---
layout: page
title: common/kate (português (Brasil))
description: "Editor de texto avançado do KDE."
content_hash: cddb44904b21c2df3049ad165a24cc944f3c50da
last_modified_at: 2024-03-01
related_topics:
  - title: English version
    url: /en/common/kate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kate

Editor de texto avançado do KDE.
Mais informações: <https://kate-editor.org/>.

- Abre arquivos específicos:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Abre arquivos remotos específicos:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/caminho/para/arquivo1 https://example.com/caminho/para/arquivo2 ...</span>

- Cria uma uma nova instância do editor mesmo que uma já esteja aberta:

`kate --new`

- Abre um arquivo com o cursor em uma linha específica:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_linha</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo com o cursor em uma linha e coluna específica:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_linha</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_coluna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Cria um arquivo a partir do `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` | kate --stdin`

- Exibe ajuda:

`kate --help`
