---
layout: page
title: common/npm-dedupe (English)
description: "Reduce duplication in the `node_modules` directory."
content_hash: b1732814589979362a11c55d753ce00e59e8ada4
last_modified_at: 2024-10-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-dedupe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm dedupe

Reduce duplication in the `node_modules` directory.
More information: <https://docs.npmjs.com/cli/commands/npm-dedupe>.

- Deduplicate packages in `node_modules`:

`npm dedupe`

- Follow `package-lock.json` or `npm-shrinkwrap.json` during deduplication:

`npm dedupe --lock`

- Run deduplication in strict mode:

`npm dedupe --strict`

- Skip optional/peer dependencies during deduplication:

`npm dedupe --omit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional|peer</span>

- Enable detailed logging for troubleshooting:

`npm dedupe --loglevel=verbose`

- Limit deduplication to a specific package:

`npm dedupe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
