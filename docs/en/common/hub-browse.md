---
layout: page
title: common/hub-browse (English)
description: "Open a GitHub repository in the browser or print the URL."
content_hash: d8be764eb8dc1cc8a500d5eb907db189fcc64238
last_modified_at: 2023-10-25
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hub browse

Open a GitHub repository in the browser or print the URL.
More information: <https://cli.github.com/manual/hub_browse>.

- Open the homepage of the current repository in the default web browser:

`hub browse`

- Open the homepage of a specific repository in the default web browser:

`hub browse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Open the subpage of a specific repository in the default web browser, subpage can be "wiki", "commits", "issues", or other (default: "tree"):

`hub browse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subpage</span>
