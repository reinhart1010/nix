---
layout: page
title: common/gh-gist (English)
description: "Work with GitHub Gists on the command-line."
content_hash: 70ac597276256b0b30070a1d6c7806f46e0e104f
last_modified_at: 2023-05-02
related_topics:
  - title: 中文 version
    url: /zh/common/gh-gist.html
    icon: bi bi-globe
---
# gh gist

Work with GitHub Gists on the command-line.
More information: <https://cli.github.com/manual/gh_gist>.

- Create a new Gist from a space-separated list of files:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Create a new Gist with a specific [desc]ription:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` --desc "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Edit a Gist:

`gh gist edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|url</span>

- List up to 42 Gists owned by the currently logged in user:

`gh gist list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- View a Gist in the default browser without rendering Markdown:

`gh gist view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|url</span>` --web --raw`
