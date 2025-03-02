---
layout: page
title: linux/chcon (français)
description: "Change le contexte de sécurité de SELinux d'un ou plusieurs fichiers/dossiers."
content_hash: 7300b0839627602cda9f180a80564eac46534a3c
last_modified_at: 2025-03-02
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
  - title: Nederlands version
    url: /nl/linux/chcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcon

Change le contexte de sécurité de SELinux d'un ou plusieurs fichiers/dossiers.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

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
