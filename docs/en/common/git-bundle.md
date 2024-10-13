---
layout: page
title: common/git-bundle (English)
description: "Package objects and references into an archive."
content_hash: af5740e534203035d5d28f0c0d1973e889fa5640
last_modified_at: 2024-10-13
related_topics:
  - title: español version
    url: /es/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bundle

Package objects and references into an archive.
More information: <https://git-scm.com/docs/git-bundle>.

- Create a bundle file that contains all objects and references of a specific branch:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a bundle file of all branches:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` --all`

- Create a bundle file of the last 5 commits of the current branch:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` -5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Create a bundle file of the latest 7 days:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` --since 7.days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Verify that a bundle file is valid and can be applied to the current repository:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>

- Print to `stdout` the list of references contained in a bundle:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>

- Unbundle a specific branch from a bundle file into the current repository:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a new repository from a bundle:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>
