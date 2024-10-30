---
layout: page
title: freebsd/chpass (português (Brasil))
description: "Adiciona ou altera informação de usuário do banco de dados, incluindo login shell e senha."
content_hash: 0f539496de2dcdafa5129ec88dfaa9b0eba0dbac
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/freebsd/chpass.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

Adiciona ou altera informação de usuário do banco de dados, incluindo login shell e senha.
Veja também: `passwd`.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Adiciona ou altera informação de usuário do banco de dados para o usuário atual interativamente:

`su -c chpass`

- Define uma [s]hell de login para o usuário atual:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/shell</span>

- Define uma [s]hell de login para um usuário específico:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>

- Altera o tempo de [e]xpiração da conta (Unix epoch):

`su -c 'chpass -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tempo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`'`

- Altera a senha de um usuário:

`su -c 'chpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha_criptografada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`'`

- Especifica [h]ostname ou endereço de um servidor NIS para consulta:

`su -c 'chpass -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`'`

- Especifica um [d]omínio NIS específico (nome do domínio do sistema por padrão):

`su -c 'chpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domínio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`'`
