---
layout: page
title: common/git-pr (português (Brasil))
description: "Traz o código via checkout dos pull requests do GitHub localmente."
content_hash: df6ccc067f298385a88cd27e90f793150944804b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-pr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pr

Traz o código via checkout dos pull requests do GitHub localmente.
Parte do `git-extras`.
Mais informações: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Traz o código específico de um pull request:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_do_pr</span>

- Traz o código de um pull request para um remoto específico:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_do_pr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>

- Traz o código de um pull request da sua URL:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limpa pull requests antigos:

`git pr clean`
