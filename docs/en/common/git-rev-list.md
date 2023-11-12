---
layout: page
title: common/git-rev-list (English)
description: "List revisions (commits) in reverse chronological order."
content_hash: a822e98e89fd9628a54d306a4b14445baa36a74b
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-rev-list.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-list.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-list.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rev-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rev-list

List revisions (commits) in reverse chronological order.
More information: <https://git-scm.com/docs/git-rev-list>.

- List all commits on the current branch:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Print the latest commit that changed (add/edit/remove) a specific file on the current branch:

`git rev-list -n 1 HEAD -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List commits more recent than a specific date, on a specific branch:

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- List all merge commits on a specific commit:

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Print the number of commits since a specific tag:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>`..HEAD --count`
