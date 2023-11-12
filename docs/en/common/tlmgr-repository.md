---
layout: page
title: common/tlmgr-repository (English)
description: "Manage repositories of a TeX Live installation."
content_hash: c7bf879da6e342fa0ee2d8874ce22d1d103968cd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr repository

Manage repositories of a TeX Live installation.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all configured repositories and their tags (if set):

`tlmgr repository list`

- List all packages available in a specific repository:

`tlmgr repository list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|url|tag</span>

- Add a new repository with a specific tag (the tag is not required):

`sudo tlmgr repository add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Remove a specific repository:

`sudo tlmgr repository remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|url|tag</span>

- Set a new list of repositories, overwriting the previous list:

`sudo tlmgr repository set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|url|tag</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|url|tag</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Show the verification status of all configured repositories:

`tlmgr repository status`
