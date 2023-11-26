---
layout: page
title: common/hut (English)
description: "A CLI tool for sourcehut."
content_hash: 3a27d8f189a4921581cf09cc2170a5784ceb028d
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# hut

A CLI tool for sourcehut.
More information: <https://manned.org/hut>.

- Initialize `hut`'s configuration file (this will prompt for an OAuth2 access token, which is required to use `hut`):

`hut init`

- List Git/Mercurial repositories:

`hut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg</span>` list`

- Create a public Git/Mercurial repository:

`hut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg</span>` create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List jobs on <https://builds.sr.ht>:

`hut builds list`

- Show the status of a job:

`hut builds show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- SSH into a job container:

`hut ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>
