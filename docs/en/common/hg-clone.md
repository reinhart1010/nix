---
layout: page
title: common/hg-clone (English)
description: "Create a copy of an existing repository in a new directory."
content_hash: 1f515a650ecb8e6021c3053f9317a30d52dc3a98
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hg clone

Create a copy of an existing repository in a new directory.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#clone>.

- Clone a repository to a specified directory:

`hg clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_path</span>

- Clone a repository to the head of a specific branch, ignoring later commits:

`hg clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_source</span>

- Clone a repository with only the `.hg` directory, without checking out files:

`hg clone --noupdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_source</span>

- Clone a repository to a specific revision, tag or branch, keeping the entire history:

`hg clone --updaterev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_source</span>

- Clone a repository up to a specific revision without any newer history:

`hg clone --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_source</span>
