---
layout: page
title: common/gh-secret (English)
description: "Manage GitHub secrets."
content_hash: 963fed142d2e02dd98218aa7668183bfb986b1ca
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gh secret

Manage GitHub secrets.
More information: <https://cli.github.com/manual/gh_secret>.

- List secret keys for the current repository:

`gh secret list`

- List secret keys for a specific organization:

`gh secret list --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- List secret keys for a specific repository:

`gh secret list --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Set a secret for the current repository (user will be prompted for the value):

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Set a secret from a file for the current repository:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set an organization secret for specific repositories:

`gh secret set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>` --repos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository1,repository2</span>

- Remove a secret for the current repository:

`gh secret remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Remove a secret for a specific organization:

`gh secret remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>
