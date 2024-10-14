---
layout: page
title: common/zapier (English)
description: "Create, automate, and manage zapier integrations."
content_hash: 208c57873b86e81b2f95d964778d0a34f80cbbda
last_modified_at: 2024-10-14
tldri18n_status: 2
---
# zapier

Create, automate, and manage zapier integrations.
Some subcommands such as `build`, `init`, `scaffold`, `push`, `test`, etc. have their own usage documentation.
More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md>.

- Connect to a Zapier account:

`zapier login`

- Initialize a new Zapier integration with a project template:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Add a starting trigger, create, search, or resource to your integration:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|create|search|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Test an integration:

`zapier test`

- Build and upload an integration to Zapier:

`zapier push`

- Display help:

`zapier help`

- Display help for a specific command:

`zapier help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
