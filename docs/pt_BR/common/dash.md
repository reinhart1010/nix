---
layout: page
title: common/dash (português (Brasil))
description: "Debian Almquist Shell, uma implementação moderna e compatível com POSIX de `sh` (não compatível com Bash)."
content_hash: 8b034810469d20b07a9bfe891cb5848f97e790b6
last_modified_at: 2023-12-28
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
tldri18n_status: 2
---
# dash

Debian Almquist Shell, uma implementação moderna e compatível com POSIX de `sh` (não compatível com Bash).
Mais informações: <https://manned.org/dash>.

- Inicia uma sessão de shell interativa:

`dash`

- Executa [c]omandos específicos:

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'dash executado'</span>`"`

- Executa um script específico:

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Checar erros de sintaxe em um script específico:

`dash -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa comandos de um script, imprimindo cada comando antes de executá-lo:

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa comandos de um script, parando no primeiro [e]rro:

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa comandos específicos de `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'dash executado'"</span>` | dash`
