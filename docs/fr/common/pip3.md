---
layout: page
title: common/pip3 (français)
description: "Gestionnaire des paquets pour Python."
content_hash: 8b36eb782228b1cef42fc650ebcf15526eb9fad6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pip3.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip3.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pip3

Gestionnaire des paquets pour Python.
Plus d'informations : <https://pip.pypa.io>.

- Recherche un paquet :

`pip3 search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Installe un paquet :

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Installe une version particulière d'un paquet :

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Met à jour un paquet :

`pip3 install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Désinstalle un paquet :

`pip3 uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Sauvegarde une liste des paquets installés :

`pip3 freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Installe des paquets à partir d'un fichier :

`pip3 install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Affiche les informations d'un paquet installé :

`pip3 show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>
