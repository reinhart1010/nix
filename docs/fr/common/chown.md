---
layout: page
title: common/chown (français)
description: "Modifie l'utilisateur et le groupe propriétaire des fichiers et dossiers."
content_hash: 6c58ef5b9917bd4bedb9a0d5160f898707f78a12
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chown.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chown.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chown.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chown.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chown.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/chown.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chown

Modifie l'utilisateur et le groupe propriétaire des fichiers et dossiers.
Plus d'informations : <https://www.gnu.org/software/coreutils/chown>.

- Modifie le propriétaire d'un fichier/dossier :

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Modifie l'utilisateur et le groupe propriétaire d'un fichier/dossier :

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Modifie récursivement le propriétaire d'un dossier et de son contenu :

`chown -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Modifie le propriétaire d'un lien symbolique :

`chown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/lien_symbolique</span>

- Modifie le propriétaire d'un fichier / dossier pour correspondre à un fichier de référence :

`chown --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_de_référence</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>
