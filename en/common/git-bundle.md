---
layout: page
title: common/git-bundle (English)
description: "Package objects and references into an archive."
content_hash: 1c2d37d8d0462b7644ada7094d28ed924fce2886
related_topics:
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
---
# git bundle

Package objects and references into an archive.
More information: <https://git-scm.com/docs/git-bundle>.

- Create a bundle file that contains all objects and references of a specific branch:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a bundle file of all branches:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` --all`

- Create a bundle file of the last 5 commits of the current branch:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Create a bundle file of the latest 7 days:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.days</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Verify that a bundle file is valid and can be applied to the current repository:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>

- Print to the standard output the list of references contained in a bundle:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>

- Unbundle a specific branch from a bundle file into the current repository:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
