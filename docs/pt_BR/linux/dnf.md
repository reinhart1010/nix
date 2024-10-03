---
layout: page
title: linux/dnf (português (Brasil))
description: "Gerenciador de pacotes das distribuições baseadas em RHEL (substituto do yum)."
content_hash: 9bed70bf3ec475fb2f9a42eb2d17d1c5e52d5218
last_modified_at: 2024-10-03
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf

Gerenciador de pacotes das distribuições baseadas em RHEL (substituto do yum).
Para comandos equivalentes em outros gerenciadores de pacotes, veja <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Mais informações: <https://dnf.readthedocs.io>.

- Atualiza os pacotes instalados para suas versões mais atuais:

`sudo dnf upgrade`

- Busca pacotes com palavras-chave:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_chave1 palavra_chave2 ...</span>

- Mostra detalhes sobre um determinado pacote:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Instala um novo pacote (use `-y` para responder sim à todos os prompts):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote1 pacote2 ...</span>

- Remove um pacote:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote1 pacote2 ...</span>

- Lista pacotes intalados:

`dnf list --installed`

- Busca por pacotes que fornecem um dado comando:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Mostra todas as operações passadas:

`dnf history`
