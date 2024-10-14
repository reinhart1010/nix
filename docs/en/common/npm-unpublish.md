---
layout: page
title: common/npm-unpublish (English)
description: "Remove a package from the npm registry."
content_hash: a793fa248fd62bfb7602a0d5c676642859a55d60
last_modified_at: 2024-10-14
tldri18n_status: 2
---
# npm unpublish

Remove a package from the npm registry.
More information: <https://docs.npmjs.com/cli/v8/commands/npm-unpublish>.

- Unpublish a specific package version:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Unpublish the entire package:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --force`

- Unpublish a package that is scoped:

`npm unpublish @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scope</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Specify a timeout period before unpublishing:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_in_milliseconds</span>

- To prevent accidental unpublishing, use the `--dry-run` flag to see what would be unpublished:

`npm unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --dry-run`
