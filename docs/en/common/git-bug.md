---
layout: page
title: common/git-bug (English)
description: "A distributed bug tracker that uses git's internal storage, so no files are added in your project."
content_hash: 17960361a1451665286df512e2329cd7fd3fa60e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git bug

A distributed bug tracker that uses git's internal storage, so no files are added in your project.
You may submit your problems to the same git remote you use to interact with others, much like commits and branches.
More information: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- Create a new identity:

`git bug user create`

- Create a new bug:

`git bug add`

- You can push your new entry to a remote:

`git bug push`

- You can pull for updates:

`git bug pull`

- List existing bugs:

`git bug ls`

- Filter and sort bugs using a query:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edit</span>`"`

- Search for bugs by text content:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_query</span>`" baz`
