---
layout: page
title: common/gh-gist (English)
description: "Work with GitHub Gists on the command-line."
content_hash: d0f68215b61ce7024f45314c4a35399755ac60ae
related_topics:
  - title: 中文 version
    url: /zh/common/gh-gist.html
    icon: bi bi-globe
---
# gh gist

Work with GitHub Gists on the command-line.
More information: <https://cli.github.com/manual/gh_gist>.

- Create a new Gist from a space-separated list of files:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>

- Create a new Gist with a description:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` --desc "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Edit a Gist:

`gh gist edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_or_url</span>

- List Gists owned by the currently logged in user:

`gh gist list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">int</span>

- View a Gist in the default browser without rendering Markdown:

`gh gist view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_or_url</span>` --web --raw`
