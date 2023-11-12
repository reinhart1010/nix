---
layout: page
title: common/dash (português (Brasil))
description: "Debian Almquist Shell, uma implementação moderna e compatível com POSIX de `sh` (não compatível com Bash)."
content_hash: 02c65b79c204464939658d6a7435981d7337af0d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dash

Debian Almquist Shell, uma implementação moderna e compatível com POSIX de `sh` (não compatível com Bash).
Mais informações: <https://manned.org/dash>.

- Inicia uma sessão de shell interativa:

`dash`

- Executa um comando e sai:

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Executa um script:

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa comandos de um script, imprimindo cada comando antes de executá-lo:

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa comandos de um script, parando no primeiro erro:

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Lê e executa comandos de `stdin`:

`dash -s`
