---
layout: page
title: common/alias (português (Brasil))
description: "Cria apelidos -- palavras que são substituídas por um comando."
content_hash: cd158c3f177dfdbc02e7c1a3a3190b861a679e62
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/alias.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/alias.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alias.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alias.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/alias.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alias.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/alias.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alias.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alias.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/alias.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alias.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/alias.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alias.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alias.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/alias.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/alias.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alias.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alias

Cria apelidos -- palavras que são substituídas por um comando.
Apelidos expiram ao final da sessão atual do shell de comando, a menos que sejam definidos no arquivo de configuração do shell, por exemplo `~/.bashrc`.
Mais informações: <https://tldp.org/LDP/abs/html/aliases.html>.

- Criar um apelido:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apelido</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Visualizar o comando associado a um determinado apelido:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apelido</span>

- Remover um apelido:

`unalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apelido</span>

- Exibir todos os apelidos definidos:

`alias -p`

- Tornar o comando `rm` interativo:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm -i</span>`"`

- Criar o apelido `la` como um atalho para `ls -a`:

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">la</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -a</span>`"`
