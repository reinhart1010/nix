---
layout: page
title: linux/flameshot (português (Brasil))
description: "Função de captura da tela com uma Interface Gráfica do Usuário."
content_hash: 2124cf0aa915a4c06de10f84743abfd1f13ae543
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/flameshot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/flameshot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flameshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flameshot

Função de captura da tela com uma Interface Gráfica do Usuário.
Suporta edição básica de imagens, como texto, formas, cores e imgur.
Mais informações: <https://flameshot.org>.

- Cria uma captura da tela completa:

`flameshot full`

- Cria uma captura da tela interativamente:

`flameshot gui`

- Cria uma captura da tela e salva em um caminho específico:

`flameshot gui --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Cria uma captura da tela interativamente em um modo simplificado:

`flameshot launcher`

- Cria uma captura da tela a partir de um monitor específico:

`flameshot screen --number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Cria uma captura da tela e imprime na saída padrão:

`flameshot gui --raw`

- Cria uma captura da tela e copia para a área de transferência:

`flameshot gui --clipboard`

- Cria uma captura da tela com um atraso específico em milissegundos:

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
