---
layout: page
title: osx/ed (português (Brasil))
description: "Editor de texto original do Unix."
content_hash: 98b3070ac751cc9d50eba179400c04d7f1d73072
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/ed.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

Editor de texto original do Unix.
Veja também: `awk`, `sed`.
Mais informações: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia uma sessão interativa do editor com um documento vazio:

`ed`

- Inicia uma sessão interativa do editor com um documento vazio e um [p]rompt específico:

`ed -p '> '`

- Inicia uma sessão interativa do editor com um documento vazio e sem diagnósticos, contagens de bytes, e prompt '!':

`ed -s`

- Edita um arquivo específico (mostra a contagem de bytes do arquivo carregado):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Substitui uma string por uma substituição específica em todas as linhas:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressão_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substituição</span>`/g`
