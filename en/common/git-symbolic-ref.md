---
layout: page
title: common/git-symbolic-ref (English)
description: "Read, change, or delete files that store references."
content_hash: 109918b800090fe393febe890e784352dfaf2472
---
# git symbolic-ref

Read, change, or delete files that store references.
More information: <https://git-scm.com/docs/git-symbolic-ref>.

- Store a reference by a name:

`git symbolic-ref refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ref</span>

- Store a reference by name, including a message with a reason for the update:

`git symbolic-ref -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` refs/heads/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Read a reference by name:

`git symbolic-ref refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete a reference by name:

`git symbolic-ref --delete refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- For scripting, hide errors with `--quiet` and use `--short` to simplify ("refs/heads/X" prints as "X"):

`git symbolic-ref --quiet --short refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
