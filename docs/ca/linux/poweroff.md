---
layout: page
title: linux/poweroff (català)
description: "Apaga la màquina."
content_hash: 3fe2fa48232187b88484177bbe171cf91370f109
last_modified_at: 2024-06-19
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
Més informació: <https://www.manned.org/poweroff>.

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
