---
layout: page
title: common/npm-dedupe (English)
description: "Reduce duplication in the `node_modules` directory."
content_hash: b1732814589979362a11c55d753ce00e59e8ada4
last_modified_at: 2024-10-31
tldri18n_status: 2
---
# npm dedupe

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
