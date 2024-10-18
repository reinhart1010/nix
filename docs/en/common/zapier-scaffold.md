---
layout: page
title: common/zapier-scaffold (English)
description: "Add a starting trigger, create, search, or resource to an integration."
content_hash: 29258add3bc495d0378f2a206ece24dcf869d04f
last_modified_at: 2024-10-18
tldri18n_status: 2
---
# zapier scaffold

Add a starting trigger, create, search, or resource to an integration.
More information: <https://platform.zapier.com/reference/cli#scaffold>.

- Scaffold a new trigger, create, search, or resource:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">noun</span>

- Specify a custom destination directory for the scaffolded files:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">noun</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--dest</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Overwrite existing files when scaffolding:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">noun</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Exclude comments from the scaffolded files:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">noun</span>` --no-help`

- Show extra debugging output:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
