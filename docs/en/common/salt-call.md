---
layout: page
title: common/salt-call (English)
description: "Invoke salt locally on a salt minion."
content_hash: 785d07c7c006769240a34a09c7398122e926349f
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# salt-call

Invoke salt locally on a salt minion.
More information: <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>.

- Perform a highstate on this minion:

`salt-call state.highstate`

- Perform a highstate dry-run, compute all changes but don't actually perform them:

`salt-call state.highstate test=true`

- Perform a highstate with verbose debugging output:

`salt-call -l debug state.highstate`

- List this minion's grains:

`salt-call grains.items`
