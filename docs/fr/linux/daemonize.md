---
layout: page
title: linux/daemonize (français)
description: "Lance une commande (qui ne se \"démonise\" pas elle-même) comme démon UNIX."
content_hash: 64930404d8a0dd137d98944cc231472020dab1cd
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/linux/daemonize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# daemonize

Lance une commande (qui ne se "démonise" pas elle-même) comme démon UNIX.
Plus d'informations : <https://software.clapper.org/daemonize/>.

- Lance une commande comme démon :

`daemonize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_de_commande</span>

- Écrit le PID dans le fichier spécifié :

`daemonize -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier/pid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_de_commande</span>

- Utilise un fichier verrou pour s'assurer que seulement une instance fonctionne à la fois :

`daemonize -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier/verrou</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_de_commande</span>

- Utilise le compte utilisateur spécifié :

`sudo daemonize -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_de_commande</span>
