---
layout: page
title: common/git-notes (français)
description: "Ajoute ou inspecte des notes d'objets."
content_hash: fcb167dafd75361722799c0373f341c967f67316
related_topics:
  - title: English version
    url: /en/common/git-notes.html
    icon: bi bi-globe
---
# git notes

Ajoute ou inspecte des notes d'objets.
Plus d'informations : <https://git-scm.com/docs/git-notes>.

- Lister toutes les notes et leurs objets rattachés :

`git notes list`

- Lister toutes les notes attachées à un objet donné :

`git notes list [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet</span>`]`

- Afficher les notes attachées à un objet donné :

`git notes show [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet</span>`]`

- Ajoute une note à un objet donné :

`git notes append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet</span>

- Ajoute une note à un objet donné, en spécifiant le message :

`git notes append --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texte_du_message</span>`"`

- Édite une note existante :

`git notes edit [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet</span>`]`

- Copie la note d'un objet vers un autre :

`git notes copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet_cible</span>

- Supprime toutes les notes d'un objet donné :

`git notes remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objet</span>
