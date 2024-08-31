---
layout: page
title: common/git-cherry (English)
description: "Find commits that have yet to be applied upstream."
content_hash: 6f3adf6d36845d117bff1b670cf1c73d699d3d73
last_modified_at: 2024-08-31
related_topics:
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cherry.html
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

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--verbose|-v</span>

- Specify a different upstream and topic branch:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Limit commits to those within a given limit:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
