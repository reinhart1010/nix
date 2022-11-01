---
layout: page
title: linux/chcon (français)
description: "Change le contexte de sécurité de SELinux d'un ou plusieurs fichiers/dossiers."
content_hash: 9f7dd915bb7a32ec0141b1e043397479faf7a22f
related_topics:
  - title: English version
    url: /en/linux/chcon.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/chcon.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/chcon.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chcon

Change le contexte de sécurité de SELinux d'un ou plusieurs fichiers/dossiers.
Plus d'information : <https://www.gnu.org/software/coreutils/chcon>.

- Affiche le contexte de sécurité d'un fichier :

`ls -lZ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Change le contexte de sécurité d'un fichier cible, en utilisant un fichier de référence :

`chcon --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_référence</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_cible</span>

- Change le contexte de sécurité SELinux complet d'un fichier :

`chcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range/level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Change seulement la partie utilisateur du contexte de sécurité SELinux :

`chcon -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Change seulement la partie role du contexte de sécurité SELinux :

`chcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Change seulement la partie type du contexte de sécurité SELinux :

`chcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Change seulement la partie plage/niveau du contexte de sécurité SELinux :

`chcon -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plage/niveau</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>
