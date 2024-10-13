---
layout: page
title: common/git-cherry (français)
description: "Rechercher des commits qui n'ont pas encore été appliqués en amont."
content_hash: f638b9a99a762a61b95e600cbfdc164a34f59248
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cherry.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry

Rechercher des commits qui n'ont pas encore été appliqués en amont.
Plus d'informations : <https://git-scm.com/docs/git-cherry>.

- Afficher les commits (et leurs messages) avec des commits équivalents en amont :

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Spécifiez une branche amont et une branche de rubrique différentes :

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Limiter les commits à ceux dans la limite donnée :

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
