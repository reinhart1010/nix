---
layout: page
title: linux/ac (français)
description: "Affiche les statistiques concernant la durée de connexion des utilisateurs."
content_hash: 848cef8332eb324626aebfb0eb7868aa03a8122b
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

Affiche les statistiques concernant la durée de connexion des utilisateurs.
Plus d'informations : <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Affiche pendant combien de temps l'utilisateur actuel a été connecté, en heures :

`ac`

- Affiche pendant combien de temps les utilisateurs ont été connectés, en heures :

`ac --individual-totals`

- Affiche pendant combien de temps un utilisateur particulier a été connecté, en heures :

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>

- Affiche pendant combien de temps un utilisateur particulier a été connecté, en heures par jour (avec le total) :

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>

- Affiche des détails supplémentaires :

`ac --compatibility`
