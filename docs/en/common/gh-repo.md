---
layout: page
title: common/gh-repo (English)
description: "Work with GitHub repositories on the command-line."
content_hash: c158298140ffe76e5db6009077bfadf650141fd1
related_topics:
  - title: 中文 version
    url: /zh/common/gh-repo.html
    icon: bi bi-globe
---
# gh repo

Work with GitHub repositories on the command-line.
More information: <https://cli.github.com/manual/gh_repo>.

- Create a new repository (if the repository name is not set, the default name will be the name of the current directory):

`gh repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Clone a repository:

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Fork and clone a repository:

`gh repo fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --clone`

- View a repository in the default web browser:

`gh repo view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --web`

- List repositories owned by a specific user or organization (if the owner is not set, the default owner will be the currently logged in user):

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>

- List only non-forks repositories:

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>` --non-forks`

- List repositories with a specific primary coding language:

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language_name</span>
