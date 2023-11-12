---
layout: page
title: common/git-show-ref (français)
description: "Commande Git pour lister les références."
content_hash: 0b60a233265a078cbebbcacd22407bc8ab88ea6d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-show-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show-ref.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show-ref

Commande Git pour lister les références.
Plus d'informations : <https://git-scm.com/docs/git-show-ref>.

- Affiche toutes les références dans le dépôt :

`git show-ref`

- Affiche seulement les références des têtes de branches :

`git show-ref --heads`

- Affiche seulement les références de tags :

`git show-ref --tags`

- Vérifier l'existence d'une référence :

`git show-ref --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/reference</span>
