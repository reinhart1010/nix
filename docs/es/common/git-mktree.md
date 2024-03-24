---
layout: page
title: common/git-mktree (español)
description: "Construye un objeto árbol usando texto formateado `ls-tree`."
content_hash: 732a08fd24a5c6b3e04aad343c1d7d0457e8b3aa
last_modified_at: 2024-03-24
related_topics:
  - title: English version
    url: /en/common/git-mktree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-mktree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git mktree

Construye un objeto árbol usando texto formateado `ls-tree`.
Más información: <https://git-scm.com/docs/git-mktree>.

- Construye un objeto árbol y verifica que el hash de cada entrada del árbol identifica un objeto existente:

`git mktree`

- Permite que falten objetos:

`git mktree --missing`

- Lee la salida terminada en NUL (carácter cero) del objeto árbol (`ls-tree -z`):

`git mktree -z`

- Permite la creación de múltiples objetos árbol:

`git mktree --batch`

- Ordena y construye un árbol a partir de `stdin` (se requiere un formato de salida de `git ls-tree` no recursivo):

`git mktree < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/árbol.txt</span>
