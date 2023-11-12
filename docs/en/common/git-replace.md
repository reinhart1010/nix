---
layout: page
title: common/git-replace (English)
description: "Create, list, and delete refs to replace objects."
content_hash: 97969528c2bce8be094c22b3319613ab07ea62a6
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/git-replace.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-replace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git replace

Create, list, and delete refs to replace objects.
More information: <https://git-scm.com/docs/git-replace>.

- Replace any commit with a different one, leaving other commits unchanged:

`git replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>

- Delete existing replace refs for the given objects:

`git replace --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>

- Edit an object’s content interactively:

`git replace --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>
