---
layout: page
title: sunos/svcadm (français)
description: "Manipuler les instances de service."
content_hash: ad2be6737c33c67303d1bc5f883aa77f6503c54e
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcadm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svcadm

Manipuler les instances de service.
Plus d'information : <https://www.unix.com/man-page/linux/1m/svcadm>.

- Activer un service dans la base de données de service:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>

- Désactiver le service:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>

- Redémarrer un service en cours d'exécution:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>

- Service de commande pour relire les fichiers de configuration:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>

- Effacer un service de l'état de maintenance et lui ordonner de démarrer:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_service</span>
