---
layout: page
title: common/git-format-patch (English)
description: "Prepare .patch files. Useful when emailing commits elsewhere."
content_hash: d5801433c1226d4b2e7702f20d2aa41a26e25931
last_modified_at: 2022-12-04
related_topics:
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-format-patch.html
    icon: bi bi-globe
---
# git format-patch

Prepare .patch files. Useful when emailing commits elsewhere.
See also `git am`, which can apply generated .patch files.
More information: <https://git-scm.com/docs/git-format-patch>.

- Create an auto-named `.patch` file for all the unpushed commits:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- Write a `.patch` file for all the commits between 2 revisions to `stdout`:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_2</span>

- Write a `.patch` file for the 3 latest commits:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
