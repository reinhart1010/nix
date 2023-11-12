---
layout: page
title: common/ssh (português (Brasil))
description: "O Secure Shell é um protocolo usado para fazer login de forma segura em sistemas remotos."
content_hash: 29525ce16004358da0cc97856fa939fcfb6bbc14
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ssh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh

O Secure Shell é um protocolo usado para fazer login de forma segura em sistemas remotos.
Ele pode ser usado para fazer login ou executar comandos em um servidor remoto.
Mais informações: <https://man.openbsd.org/ssh>.

- Conectar-se a um servidor remoto:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Conectar-se a um servidor remoto com uma identidade específica (chave privada):

`ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_chave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Conectar-se a um servidor remoto usando uma porta específica:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>

- Executar um comando em um servidor remoto com uma alocação de [t]ty permitindo interação com o comando remoto:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_do_comando</span>

- Tunelamento SSH: Encaminhamento dinâmico de porta (proxy SOCKS em `localhost:1080`):

`ssh -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Tunelamento SSH: Encaminhar uma porta específica (`localhost:9999` para `example.org:80`), desativar alocação de pseudo-[t]ty e execução de comandos remotos:

`ssh -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -N -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Saltar com SSH: Conectar-se a um servidor remoto através de um host intermediário (vários saltos intermediários podem ser especificados separados por vírgula):

`ssh -J `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_intermediário</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Encaminhamento do agente: Encaminhar as informações de autenticação para a máquina remota (consulte `man ssh_config` para opções disponíveis):

`ssh -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>
