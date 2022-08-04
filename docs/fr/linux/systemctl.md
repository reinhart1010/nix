---
layout: page
title: linux/systemctl (français)
description: "Contrôle le système systemd et le gestionnaire de services."
content_hash: 4e6a59706694d30adf5cb0dda49a8a8df8a5a3b5
related_topics:
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
---
# systemctl

Contrôle le système systemd et le gestionnaire de services.
Plus d'informations : <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Liste des unités en échec :

`systemctl --failed`

- Démarre/arrête/redémarre/recharge un service :

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unité</span>

- Affiche le statut d'une unité :

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unité</span>

- Active/désactive une unité à démarrer au démarrage :

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unité</span>

- Masque/démasque une unité pour empêcher l'activation et l'activation manuelle :

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unité</span>

- Rechargement de systemd, recherche d'unités nouvelles ou modifiées :

`systemctl daemon-reload`

- Vérifie si une unité est en cours de fonctionnement :

`systemctl is-active `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unité</span>

- Vérifie si une unité est activée :

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unité</span>
