---
layout: page
title: linux/poweroff (català)
description: "Apaga la màquina."
content_hash: 5979587eebd396f9fee34c2a8e0d74bac7311211
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/poweroff.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/poweroff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/poweroff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/poweroff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/poweroff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/poweroff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# poweroff

Apaga la màquina.
Més informació: <https://www.man7.org/linux/man-pages/man8/poweroff.8.html>.

- Apaga la màquina:

`poweroff`

- Atura el sistema (el mateix que `halt`):

`poweroff --halt`

- Reinicia el ssitema (el mateix que `reboot`):

`poweroff --reboot`

- Apaga el sistema sense contactar l'administrador del sistema:

`poweroff --force --force`

- Escriu l'entrada de wtpm shutdown sense apagar l'ordinador:

`poweroff --wtmp-only`
