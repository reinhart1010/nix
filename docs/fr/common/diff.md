---
layout: page
title: common/diff (français)
description: "Compare deux fichiers ou répertoires."
content_hash: 70714d9d75f392c67224acc3b00d369ba274ea95
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/diff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diff.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/diff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diff

Compare deux fichiers ou répertoires.
Plus d'informations : <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Compare deux fichiers (liste les changements pour transformer `ancien_fichier` en `nouveau_fichier`) :

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>

- Compare deux fichiers, en ignorant l'espacement :

`diff --ignore-all-space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>

- Compare deux fichiers, en affichant différences côte à côte :

`diff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>

- Compare deux fichiers, en affichant les différences dans un format unifié (comme `git diff`) :

`diff --unified `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>

- Compare récursivement deux répertoires directories (affiche les noms de fichiers et de répertoires divergents ainsi que les modifications de fichiers) :

`diff --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_répertoire</span>

- Compare deux répertoires, en affichant uniquement les fichiers qui diffèrent :

`diff --recursive --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_répertoire</span>

- Crée un fichier patch des différences entre deux fichiers texte pour Git, en traitant les fichiers inexistants comme fichiers vides :

`diff --text --unified --new-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.patch</span>
