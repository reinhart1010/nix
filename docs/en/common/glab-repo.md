---
layout: page
title: common/glab-repo (English)
description: "Work with GitLab repositories."
content_hash: 61b6938e2a7ee62f65e9592d56fab322bbfea44e
last_modified_at: 2023-07-16
---
# glab repo

Work with GitLab repositories.
More information: <https://glab.readthedocs.io/en/latest/repo/index.html#synopsis>.

- Create a new repository (if the repository name is not set, the default name will be the name of the current directory):

`glab repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Clone a repository:

`glab repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Fork and clone a repository:

`glab repo fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --clone`

- View a repository in the default web browser:

`glab repo view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --web`

- Search some repositories in the GitLab instance:

`glab repo search -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>
