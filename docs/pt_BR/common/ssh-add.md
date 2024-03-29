---
layout: page
title: common/ssh-add (português (Brasil))
description: "Gerencia as chaves SSH carregadas no ssh-agent."
content_hash: 3b395bb1c79c925ab5dd025b20f3716118e9643f
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/ssh-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ssh-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-add

Gerencia as chaves SSH carregadas no ssh-agent.
Certifique-se de que o ssh-agent esteja em execução para que as chaves sejam carregadas nele.
Mais informações: <https://man.openbsd.org/ssh-add>.

- Adiciona as chaves SSH padrão em `~/.ssh` ao ssh-agent:

`ssh-add`

- Adiciona uma chave específica ao ssh-agent:

`ssh-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/chave_privada</span>

- Lista as impressões digitais das chaves carregadas atualmente:

`ssh-add -l`

- Exclui uma chave do ssh-agent:

`ssh-add -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/chave_privada</span>

- Exclui todas as chaves carregadas atualmente do ssh-agent:

`ssh-add -D`

- Adiciona uma chave ao ssh-agent e ao keychain:

`ssh-add -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/chave_privada</span>
