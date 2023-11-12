---
layout: page
title: common/git-submodule (English)
description: "Inspects, updates and manages submodules."
content_hash: e7a38bca58b4e6b82c18ab9dd707a771ea91afbf
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-submodule.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-submodule.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-submodule.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-submodule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git submodule

Inspects, updates and manages submodules.
More information: <https://git-scm.com/docs/git-submodule>.

- Install a repository's specified submodules:

`git submodule update --init --recursive`

- Add a Git repository as a submodule:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Add a Git repository as a submodule at the specified directory:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Update every submodule to its latest commit:

`git submodule foreach git pull`
