---
layout: page
title: common/git-cherry (English)
description: "Find commits that have yet to be applied upstream."
content_hash: 1d520afcc19b9b95a18b64ba7761ba5b09d1cbff
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry

Find commits that have yet to be applied upstream.
More information: <https://git-scm.com/docs/git-cherry>.

- Show commits (and their messages) with equivalent commits upstream:

`git cherry -v`

- Specify a different upstream and topic branch:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Limit commits to those within a given limit:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
