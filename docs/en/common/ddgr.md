---
layout: page
title: common/ddgr (English)
description: "Commandline utility to search DuckDuckGo (html version) from the terminal."
content_hash: c1d966e9e99b3cc83cd9728c178e609a16b3f0ff
last_modified_at: 2023-10-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ddgr

Commandline utility to search DuckDuckGo (html version) from the terminal.
More information: <https://github.com/jarun/ddg>.

- Start interactive mode:

`ddgr`

- Search DuckDuckGo for a keyword:

`ddgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Limit the search results number to N:

`ddgr -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Show the complete URL in search results:

`ddgr -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search DuckDuckGo for a keyword and open the first result in the browser:

`ddgr !w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Perform a website specific search:

`ddgr -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">site</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search for a specific file type:

`ddgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` filetype:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filetype</span>

- Display help in interactive mode:

`?`
