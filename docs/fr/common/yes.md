---
layout: page
title: common/yes (français)
description: "Envoie un message à répétition en sortie console."
content_hash: d7776c86ef6b66571ba786f92c9939f1c9a50711
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yes

Envoie un message à répétition en sortie console.
Cette commande est souvent utilisée pour éviter de devoir accepter des opérations successives (par exemple des installations via la commande `apt-get`).
Plus d'informations : <https://www.gnu.org/software/coreutils/yes>.

- Envoyer « message » à répétition :

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Envoyer « y » à répétition :

`yes`

- Répondre « oui » à toutes les questions posées par la commande `apt-get` :

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
