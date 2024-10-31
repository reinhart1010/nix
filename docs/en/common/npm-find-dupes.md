---
layout: page
title: common/npm-find-dupes (English)
description: "Identify duplicate dependencies in `node_modules`."
content_hash: fea4fa529d10291fe8627c453042e1160a26e89b
last_modified_at: 2024-10-31
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-find-dupes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm find-dupes

Identify duplicate dependencies in `node_modules`.
More information: <https://docs.npmjs.com/cli/commands/npm-find-dupes>.

- List all duplicate packages within `node_modules`:

`npm find-dupes`

- Include `devDependencies` in duplicate detection:

`npm find-dupes --include=dev`

- List all duplicate instances of a specific package in `node-modules`:

`npm find-dupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Exclude optional dependencies from duplicate detection:

`npm find-dupes --omit=optional`

- Set the logging level for output:

`npm find-dupes --loglevel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">silent|error|warn|info|verbose</span>

- Output duplicate information in JSON format:

`npm find-dupes --json`

- Limit duplicate search to specific scopes:

`npm find-dupes --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@scope1,@scope2</span>

- Exclude specific scopes from duplicate detection:

`npm find-dupes --omit-scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@scope1,@scope2</span>
