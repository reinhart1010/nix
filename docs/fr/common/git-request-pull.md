---
layout: page
title: common/git-request-pull (français)
description: "Générer une requête demandant au projet en amont d'inclure les modifications dans son arborescence."
content_hash: 4ba2151322a6fea35600ad6d9da1217fab710065
related_topics:
  - title: English version
    url: /en/common/git-request-pull.html
    icon: bi bi-globe
---
# git request-pull

Générer une requête demandant au projet en amont d'inclure les modifications dans son arborescence.
Plus d'informations : <https://git-scm.com/docs/git-request-pull>.

- Produire une requête résumant les changements entre la version v1.1 et le master :

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Produire une requête résumant les changements entre la version v1.1 sur la branche master et la branche locale foo :

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master:foo</span>
