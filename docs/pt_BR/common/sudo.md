---
layout: page
title: common/sudo (português (Brasil))
description: "Executa um único comando como o Superuser, ou como outro usuário."
content_hash: dd564e2b769f86e9cf9a3379f02bb7c36c49fbcf
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/sudo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/sudo.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sudo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sudo

Executa um único comando como o Superuser, ou como outro usuário.
Mais informações: <https://www.sudo.ws/sudo.html>.

- Executa um comando como Superuser:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Edita um arquivo, como Superuser, com seu editor padrão:

`sudo --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Executa um comando como outro usuário e/ou grupo:

`sudo --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --group=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a}</span>

- Executa um comando anterior com o prefixo `sudo` (apenas em `bash`, `zsh`, etc.):

`sudo !!`

- Abre o shell padrão com privilégios de Superuser e executar arquivos de login (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Abre o shell padrão com privilégios de Superuser sem alterar o ambiente de execução:

`sudo --shell`

- Abre o shell padrão como dado usuário, carregando o ambiente de execução deste usuário e lendo arquivos de login (`.profile`, `.bash_profile`, etc.):

`sudo --login --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>

- Lista os comandos permitidos (e não permitidos) para o usuário atual:

`sudo --list`
