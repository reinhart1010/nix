---
layout: page
title: linux/yaourt (português (Brasil))
description: "Utilitário de Arch Linux para compilaçào de pacotes AUR (Arch User Repository)."
content_hash: e424870e42db7bea08b1c4c2289df26f607ac6f3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/yaourt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yaourt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaourt

Utilitário de Arch Linux para compilaçào de pacotes AUR (Arch User Repository).
Mais informações: <https://linuxcommandlibrary.com/man/yaourt>.

- Sincroniza e atualiza todos os pacotes (incluindo AUR):

`yaourt -Syua`

- Instala um novo pacote (incluindo AUR):

`yaourt -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remove um pacote e suas dependências (incluindo pacotes AUR):

`yaourt -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Procura no banco de dados de pacotes por uma palavra-chave (incluindo AUR):

`yaourt -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Lista pacotes instalados, versões, e repositórios (pacotes AUR serão listados sob como repositório 'local'):

`yaourt -Q`
