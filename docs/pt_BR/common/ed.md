---
layout: page
title: common/ed (português (Brasil))
description: "O editor de texto original do Unix."
content_hash: b54bd73930b7f2ce7ddca99577984c8e3cec1d00
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

O editor de texto original do Unix.
Veja também: `awk`, `sed`.
Mais informações: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia uma sessão do editor interativo com um documento vazio:

`ed`

- Inicia uma sessão do editor interativo com um documento vazio e um prompt específico:

`ed --prompt='> '`

- Inicia uma sessão do editor interativo com erros compreensíveis para usuários:

`ed --verbose`

- Inicia uma sessão do editor interativo com um documento vazio e sem diagnósticos, contagens de bytes e prompt "!":

`ed --quiet`

- Inicia uma sessão do editor interativo sem mudança no status de saída quando o comando falha:

`ed --loose-exit-status`

- Edita um arquivo específico (mostra a contagem de bytes do arquivo carregado):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Substitui a string com um substituto específico em todas as linhas:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substituto</span>`/g`
