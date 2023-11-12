---
layout: page
title: linux/yay (português (Brasil))
description: "Yet Another Yogurt: Um utilitário de Arch Linux para compilar e instalar pacotes do AUR (Arch User Repository)."
content_hash: d5b7aa38483d7005300d73bbb06d50a4eb26d3d7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/yay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yay.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/yay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yay

Yet Another Yogurt: Um utilitário de Arch Linux para compilar e instalar pacotes do AUR (Arch User Repository).
Veja também `pacman`.
Mais informações: <https://github.com/Jguer/yay>.

- Busca interativamente e instala pacotes dos repositórios e AUR:

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote|termo_de_busca</span>

- Sincroniza e atualiza todos os pacotes dos repositórios e AUR:

`yay`

- Sincroniza e atualiza apenas pacotes AUR:

`yay -Sua`

- Instala um novo pacote de repositório e AUR:

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remove um pacote instalado, suas dependências e arquivos de configuração:

`yay -Rns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Procura no banco de dados de pacotes por uma palavra-chave dos repositórios e AUR:

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_chave</span>

- Remove pacotes órfãos (instalado como dependência mas não utilizado por qualquer pacote):

`yay -Yc`

- Mostra estatísticas dos pacotes instalados e condição do sistema:

`yay -Ps`
