---
layout: page
title: common/git-update-ref (English)
description: "Git command for creating, updating, and deleting Git refs."
content_hash: 888919f0e8676ae8c612b693a5f612706d32cc8f
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/git-update-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-update-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-ref.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git update-ref

Git command for creating, updating, and deleting Git refs.
More information: <https://git-scm.com/docs/git-update-ref>.

- Delete a ref, useful for soft resetting the first commit:

`git update-ref -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Update ref with a message:

`git update-ref -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4e95e05</span>
