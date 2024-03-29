---
layout: page
title: common/git-tag (English)
description: "Create, list, delete or verify tags."
content_hash: 409e15460b3df08465d3d1d6afe2efaf7f001310
last_modified_at: 2024-02-15
related_topics:
  - title: Deutsch version
    url: /de/common/git-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-tag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git tag

Create, list, delete or verify tags.
A tag is a static reference to a commit.
More information: <https://git-scm.com/docs/git-tag>.

- List all tags:

`git tag`

- Create a tag with the given name pointing to the current commit:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Create a tag with the given name pointing to a given commit:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Create an annotated tag with the given message:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_message</span>

- Delete the tag with the given name:

`git tag -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Get updated tags from upstream:

`git fetch --tags`

- List all tags whose ancestors include a given commit:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
