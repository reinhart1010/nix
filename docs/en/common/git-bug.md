---
layout: page
title: common/git-bug (English)
description: "A distributed bug tracker that uses Git's internal storage, so no files are added in your project."
content_hash: f5e78c7d80864abe4c596cc5ed9a04b2eaa6ce07
last_modified_at: 2024-04-26
related_topics:
  - title: Indonesia version
    url: /id/common/git-bug.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bug

A distributed bug tracker that uses Git's internal storage, so no files are added in your project.
You may submit your problems to the same Git remote you use to interact with others, much like commits and branches.
More information: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- Create a new identity:

`git bug user create`

- Create a new bug:

`git bug add`

- Push a new bug entry to a remote:

`git bug push`

- Pull for updates:

`git bug pull`

- List existing bugs:

`git bug ls`

- Filter and sort bugs using a query:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edit</span>`"`

- Search for bugs by text content:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_query</span>`" baz`
