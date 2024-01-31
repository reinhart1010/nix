---
layout: page
title: common/gh-gist (English)
description: "Work with GitHub Gists."
content_hash: 58ead0b9ceab408c8cc6405fb8dbc688f318f81a
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/common/gh-gist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh gist

Work with GitHub Gists.
More information: <https://cli.github.com/manual/gh_gist>.

- Create a new Gist from one or more files:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Create a new Gist with a specific [desc]ription:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` --desc "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Edit a Gist:

`gh gist edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|url</span>

- List up to 42 Gists owned by the currently logged in user:

`gh gist list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- View a Gist in the default browser without rendering Markdown:

`gh gist view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|url</span>` --web --raw`
