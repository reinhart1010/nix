---
layout: page
title: common/gh-browse (English)
description: "Open a GitHub repository in the browser or print the URL."
content_hash: 94ceda0798be5a2f590081964cab2da266a0c579
---
# gh browse

Open a GitHub repository in the browser or print the URL.
More information: <https://cli.github.com/manual/gh_browse>.

- Open the homepage of the current repository in the default web browser:

`gh browse`

- Open the homepage of a specific repository in the default web browser:

`gh browse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Open the settings page of the current repository in the default web browser:

`gh browse --settings`

- Open the wiki of the current repository in the default web browser:

`gh browse --wiki`

- Open a specific issue or pull request in the web browser:

`gh browse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_or_pull_request_number</span>

- Open a specific branch in the web browser:

`gh browse --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Open a specific file or directory of the current repository in the web browser:

`gh browse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path_from_root_of_repository</span>

- Print the destination URL without open the web browser:

`gh browse --no-browser`
