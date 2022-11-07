---
layout: page
title: common/railway (English)
description: "Connect code to a Railway project from the command line."
content_hash: 8e487e3cd76c315a7c0fbad6e26ea83e128956dc
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># railway

Connect code to a Railway project from the command line.
More information: <https://railway.app/>.

- Login to a Railway account:

`railway login`

- Link to an existing Project under a Railway account or team:

`railway link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">projectId</span>

- Create a new project directly from the command line:

`railway init`

- Run a local command using variables from the active environment:

`railway run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmd</span>

- Deploy the linked project directory (if running from a subdirectory, the project root is still deployed):

`railway up`

- Open an interactive shell to a database:

`railway connect`
