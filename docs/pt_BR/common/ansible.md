---
layout: page
title: common/ansible (português (Brasil))
description: "Gerencia grupos de computadores remotamente utilizando SSH. (use o arquivo `/etc/ansible/hosts` para adicionar novos grupos/hosts)."
content_hash: fa660ecd549c766a7cf0bbb294b7d0b500dd9362
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible

Gerencia grupos de computadores remotamente utilizando SSH. (use o arquivo `/etc/ansible/hosts` para adicionar novos grupos/hosts).
Alguns subcomando como `ansible galaxy` possuis a própria documentação de uso.
Mais informações: <https://www.ansible.com/>.

- Lista os hosts pertencentes a um grupo:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` --list-hosts`

- Realiza o ping de um grupo de hosts invocando o módulo ping:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -m ping`

- Exibe fatos sobre um grupo de hosts invocando o módulo setup:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -m setup`

- Executa um comando em um grupo de hosts invocando o módulo command com argumentos:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meu_comando</span>`'`

- Executa um comando com privilégios administrativos:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meu_comando</span>`'`

- Executa um comando usando um arquivos de inventário customizado:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_inventario</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meu_comando</span>`'`

- Lista os grupos presentes em um inventário:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
