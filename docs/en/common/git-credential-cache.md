---
layout: page
title: common/git-credential-cache (English)
description: "Git helper to temporarily store passwords in memory."
content_hash: 4ba4c4fb3e8332b2f63fe842d319266ae5bf7251
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git credential-cache

Git helper to temporarily store passwords in memory.
More information: <https://git-scm.com/docs/git-credential-cache>.

- Store Git credentials for a specific amount of time:

`git config credential.helper 'cache --timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_in_seconds</span>`'`
