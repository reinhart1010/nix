---
layout: page
title: common/pip (français)
description: "Gestionnaire des paquets pour Python."
content_hash: 18c4ac5a3f8715f3b85782aba6ffd58b60081e8a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/pip.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pip

Gestionnaire des paquets pour Python.
Certaines commandes comme `pip install` ont leur propre documentation.
Plus d'informations : <https://pip.pypa.io>.

- Installe un paquet :

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Installe une version particulière d'un paquet :

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Installe un paquet dans le répertoire utilisateur au lieu de l'emplacement par défaut système :

`pip install --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Met à jour un paquet :

`pip install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Désinstalle un paquet :

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Sauvegarde une liste des paquets installés :

`pip freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Installe des paquets à partir d'un fichier :

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Affiche les informations d'un paquet installé :

`pip show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>
