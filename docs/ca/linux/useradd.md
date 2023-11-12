---
layout: page
title: linux/useradd (català)
description: "Crea un nou usuari."
content_hash: ac55b9aca95403154618148263b60fab8d44bf1a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/useradd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/useradd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/useradd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# useradd

Crea un nou usuari.
Vegeu també: `users`, `userdel`, `usermod`.
Més informació: <https://manned.org/useradd>.

- Crea un usuari nou:

`sudo useradd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Crea un usuari amb l'id d'usuari especificada:

`sudo useradd --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Crea un usuari nou amb una shell específica:

`sudo useradd --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Crea un usuari nou pertanyent a grups adicionals (cal tenir en compte que no existeixen espais en blanc):

`sudo useradd --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup1,grup2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Crea un usuari nou amb el directori home predeterminat:

`sudo useradd --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Crea un usuari nou amb el directori home omplert per una plantilla:

`sudo useradd --skel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cami/al/directori_plantilles</span>` --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Crea un usuari nou del sistema sense directori home:

`sudo useradd --no-create-home --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>
