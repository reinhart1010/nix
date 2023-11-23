---
layout: page
title: common/docker-rm (français)
description: "Supprime un ou plusieurs conteneurs."
content_hash: 6d795d2be3a6fdc63e9ed0e9b1d67a79542f466c
last_modified_at: 2023-11-23
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker rm

Supprime un ou plusieurs conteneurs.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/rm>.

- Supprimer des conteneurs :

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur1 conteneur2 ...</span>

- Supprimer des conteneurs par la force :

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur1 conteneur2 ...</span>

- Supprimer un conteneur et ses volumes :

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteneur</span>

- Affiche l'aide :

`docker rm`
