---
layout: page
title: common/argocd (français)
description: "Interface en ligne de commande pour controler un serveur Argo CD."
content_hash: cfb50c239a554fd1f2c8904cdc4fee19ef0e4249
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/argocd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argocd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd

Interface en ligne de commande pour controler un serveur Argo CD.
Certaines sous-commandes comme `argocd app` ont leur propre documentation d'utilisation.
Plus d'informations : <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Se connecter à un serveur Argo CD :

`argocd login --insecure --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serveur_argocd:port</span>

- Liste des applications :

`argocd app list`
