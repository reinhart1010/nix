---
layout: page
title: common/git-cherry (français)
description: "Rechercher des commits qui n'ont pas encore été appliqués en amont."
content_hash: 5d056f6580fc78285fa4feca70df3927f9fb82fa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry

Rechercher des commits qui n'ont pas encore été appliqués en amont.
Plus d'informations : <https://git-scm.com/docs/git-cherry>.

- Afficher les commits (et leurs messages) avec des commits équivalents en amont :

`git cherry -v`

- Spécifiez une branche amont et une branche de rubrique différentes :

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Limiter les commits à ceux dans la limite donnée :

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
