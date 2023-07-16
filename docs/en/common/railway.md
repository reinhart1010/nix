---
layout: page
title: common/railway (English)
description: "Connect code to a Railway project."
content_hash: 44e428cf2edd13e04ea49e866d992918d6cc8787
last_modified_at: 2023-07-16
---
# railway

Connect code to a Railway project.
More information: <https://railway.app/>.

- Login to a Railway account:

`railway login`

- Link to an existing Project under a Railway account or team:

`railway link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">projectId</span>

- Create a new project:

`railway init`

- Run a local command using variables from the active environment:

`railway run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmd</span>

- Deploy the linked project directory (if running from a subdirectory, the project root is still deployed):

`railway up`

- Open an interactive shell to a database:

`railway connect`
