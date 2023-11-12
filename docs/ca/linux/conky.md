---
layout: page
title: linux/conky (català)
description: "Monitor de sistema lleuger per X."
content_hash: dc5b6279f7af189fc450eab08d52b98699b5b9e5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/conky.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/conky.html
    icon: bi bi-globe
tldri18n_status: 2
---
# conky

Monitor de sistema lleuger per X.
Més informació: <https://github.com/brndnmtthws/conky>.

- Executa amb la configuració per defecte:

`conky`

- Crea una nova configuració per defecte:

`conky -C > ~/.conkyrc`

- Executa conky amb un arxiu de configuració concret:

`conky -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/configuració</span>

- Executa en segon pla (*daemon*):

`conky -d`

- Posiciona conky en l'escriptori:

`conky -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{top,bottom,middle}_{left,right,middle}</span>

- Pausa de 5 segons al iniciar abans d'executar-lo:

`conky -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
