---
layout: page
title: common/git-log (português (Brasil))
description: "Mostra um histórico de commits."
content_hash: cd71d7e01ea0f6b66cd1102e248269d99fb5042f
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-log.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git log

Mostra um histórico de commits.
Mais informações: <https://git-scm.com/docs/git-log>.

- Mostra a sequência de commits a partir do atual, em ordem cronológica reverse do repositório Git no diretório de trabalho atual:

`git log`

- Mostra o histórico de um arquivo ou diretório determinado, incluindo diferenças:

`git log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|-u|--patch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Mostra uma visão geral do(s) arquivo(s) alterado(s) em cada commit:

`git log --stat`

- Mostra um grafo dos commits no branch atual usando apenas a primera linha de cada mensagem de commit:

`git log --oneline --graph`

- Mostra um grafo de todos os commits, etiquetas e branches em todo o repositório:

`git log --oneline --decorate --all --graph`

- Mostra apenas os commits cujas mensagem incluem uma determinada cadeia de caracteres (sem distinção entre maiúsculas e minúsculas):

`git log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--regexp-ignore-case</span>` --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadeia_de_caracteres_para_pesquisa</span>

- Mostra os últimos N commits de um determinado autor:

`git log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--max-count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` --author "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>`"`

- Mostra os commits entre duas datas(aaaa-mm-dd):

`git log --before "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
