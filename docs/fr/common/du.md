---
layout: page
title: common/du (français)
description: "Utilisation de disque : estime et résume l'utilisation de l'espace occupé par les fichiers et les répertoires."
content_hash: dd15e6466742e61af9d3ae6b3bd7f200de37ee4b
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Utilisation de disque : estime et résume l'utilisation de l'espace occupé par les fichiers et les répertoires.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Liste les tailles d'un répertoire et de ses sous-répertoires, dans l'unité donnée (o/Kio/Mio) :

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Liste les tailles d'un répertoire et de ses sous-répertoires, sous une forme lisible par l'homme (c'est-à-dire en sélectionnant automatiquement l'unité appropriée pour chaque taille) :

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Affiche la taille d'un répertoire unique, en unités lisibles par l'homme :

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Liste les tailles, en unités lisibles par l'homme, d'un répertoire et de tous les fichiers et répertoires qu'il contient :

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Liste les tailles, en unités lisibles par l'homme, d'un répertoire et de ses sous-répertoires, jusqu'à N niveaux de profondeur :

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Liste la taille, en unités lisible par l'homme, de tous les fichiers `.jpg` dans les sous-répertoires du répertoire courant, et affiche un total cumulatif à la fin :

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>

- Liste tous les fichiers et répertoires (y compris les fichiers cachés) dépassant un certain seuil (utile pour déterminer ce qui occupe réellement l'espace) :

`du --all --human-readable --threshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1G|1024M|1048576K</span>` .[^.]* *`
