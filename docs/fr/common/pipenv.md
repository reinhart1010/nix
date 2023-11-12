---
layout: page
title: common/pipenv (français)
description: "Workflow de développement simple et unifié pour Python."
content_hash: b6df48da2c99d6d6a072b93ecc39286ea8535f87
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pipenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pipenv

Workflow de développement simple et unifié pour Python.
Gère les paquets et l'environnement virtuel d'un projet.
Plus d'informations : <https://pypi.org/project/pipenv>.

- Crée un nouveau projet :

`pipenv`

- Crée un nouveau projet à l'aide de Python 3 :

`pipenv --three`

- Installe un paquet :

`pipenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Installe toutes les dépendances d'un projet :

`pipenv install`

- Installe toutes les dépendances d'un projet (y compris les paquets de développement) :

`pipenv install --dev`

- Désinstalle un paquet :

`pipenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Démarre une session de commandes dans l'environnement virtuel :

`pipenv shell`

- Génère un `requirements.txt` (une liste de dépendances) pour un projet :

`pipenv lock --requirements`
