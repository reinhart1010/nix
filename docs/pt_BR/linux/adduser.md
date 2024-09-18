---
layout: page
title: linux/adduser (português (Brasil))
description: "Utilitário para criação de novos usuários."
content_hash: 19a8c5b4ce975b7fdc56c1fe807dd11fd41a55a3
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/adduser.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adduser

Utilitário para criação de novos usuários.
Mais informações: <https://manned.org/adduser>.

- Cria um novo usuário, o seu diretório na pasta home e solicita o preenchimento da sua senha:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Cria um novo usuário sem o seu diretório na pasta home:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Cria um novo usuário especificando a localização do seu diretório:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_da_pasta_do_usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Cria um novo usuário e configura o seu shell de login:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_o_shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Cria um novo usuário e atribuí-lo a um grupo:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>
