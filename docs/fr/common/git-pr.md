---
layout: page
title: common/git-pr (français)
description: "Récupère les pull-requests GitHub localement."
content_hash: fe531d4f2871d7a8e82b18de2d04f48a6aa04959
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-pr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-pr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pr

Récupère les pull-requests GitHub localement.
Plus d'informations : <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Récupère une pull-request spécifique :

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Récupère une pull-request d'un dépôt spécifique :

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distant</span>

- Récupère une pull-request depuis son URL :

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Nettoie les branches de pull-requests terminées :

`git pr clean`
