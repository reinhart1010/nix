---
layout: page
title: common/chmod (français)
description: "Modifie les droits d'accès d'un fichier ou d'un répertoire."
content_hash: 2361009b711bbe432aac91cca5fbd8ff5a03feaa
last_modified_at: 2024-12-05
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chmod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chmod

Modifie les droits d'accès d'un fichier ou d'un répertoire.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Donne les droits d'e[x]écution à l'[u]tilisateur auquel le fichier appartient :

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Donne à l'[u]tilisateur les droits de lecture [r] et d'écriture [w] sur un fichier/répertoire :

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire</span>

- Enlève les droits d'e[x]écution pour le [g]roupe :

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Donne à tous [a] les utilisateurs les droits de lecture [r] et d'e[x]écution :

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Donne aux autres [o] utilisateurs (qui sont dans un autre groupe) les mêmes droits que ceux du [g]roupe propriétaire :

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Retire tous les droits aux autres [o] utilisateurs :

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Modifie les permissions récursivement en donnant aux membres du [g]roupe et aux autres [o] utilisateurs le droit d'écriture [w] :

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Donne récursivement à tous [a] les utilisateurs les droits de lecture [r] de fichiers et d'e[X]écution de sous-répertoires à l'intérieur d'un répertoire :

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>
