---
layout: page
title: common/ddev (English)
description: "Container based local development tool for PHP environments."
content_hash: fdcd7107cbdddd8dd94501aa5f95bc10714147be
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ddev

Container based local development tool for PHP environments.
More information: <https://ddev.readthedocs.io>.

- Start up a project:

`ddev start`

- Configure a project's type and docroot:

`ddev config`

- [f]ollow the log trail:

`ddev logs -f`

- Run composer within the container:

`ddev composer`

- Install a specific Node.js version:

`ddev nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Export a database:

`ddev export-db --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/db.sql.gz</span>

- Run a specific command within a container:

`ddev exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 1</span>
