---
layout: page
title: common/podman-machine (português (Brasil))
description: "Criar e gerenciar máquinas virtuais executando o Podman."
content_hash: fa9cd6e7c188f0d40f588f65b6d5ed896e898931
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman-machine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman machine

Criar e gerenciar máquinas virtuais executando o Podman.
Incluído com a versão 4 ou superior do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Listar as máquinas existentes:

`podman machine ls`

- Criar uma nova máquina padrão:

`podman machine init`

- Criar uma nova máquina com um nome específico:

`podman machine init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Criar uma nova máquina com recursos diferentes:

`podman machine init --cpus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --memory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` --disk-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- Iniciar ou parar uma máquina:

`podman machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Conectar-se a uma máquina em execução via SSH:

`podman machine ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Inspecionar informações sobre uma máquina:

`podman machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
