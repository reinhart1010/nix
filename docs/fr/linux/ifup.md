---
layout: page
title: linux/ifup (français)
description: "Outil utilisé pour activer des interfaces réseau."
content_hash: de414808fd6188a6aaacd2917c062a130877ac3c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/ifup.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ifup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifup

Outil utilisé pour activer des interfaces réseau.
Plus d'informations : <https://manpages.debian.org/latest/ifupdown/ifup.8.html>.

- Active l'interface eth0 :

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Active l'ensemble des interfaces réseau définies dans le fichier `/etc/network/interfaces` :

`ifup -a`
