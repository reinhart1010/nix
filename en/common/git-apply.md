---
layout: page
title: common/git-apply (English)
description: "Apply a patch to files and/or to the index."
content_hash: 766ff8ee36fa80c6609dbab01dba37e6ca7c38fd
related_topics:
  - title: Deutsch version
    url: /de/common/git-apply.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-apply.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-apply.html
    icon: bi bi-globe
---
# git apply

Apply a patch to files and/or to the index.
More information: <https://git-scm.com/docs/git-apply>.

- Print messages about the patched files:

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Apply and add the patched files to the index:

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Apply a remote patch file:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- Output diffstat for the input and apply the patch:

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Apply the patch in reverse:

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Store the patch result in the index without modifying the working tree:

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
