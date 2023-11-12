---
layout: page
title: linux/zypper (português (Brasil))
description: "Utilitário de gerenciamento de pacotes SUSE e openSUSE."
content_hash: 023657f13ac2f1009716a5a517831322e5459578
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zypper

Utilitário de gerenciamento de pacotes SUSE e openSUSE.
Mais informações: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincroniza a lista de pacotes e versões disponíveis:

`zypper refresh`

- Instala um novo pacote:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Remove um pacote:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Atualiza os pacotes instalados para as versões mais recentes disponíveis:

`zypper update`

- Pesquisa pacote por palavra-chave:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra-chave</span>

- Mostra informações relacionadas aos repositórios configurados:

`zypper repos --sort-by-priority`
