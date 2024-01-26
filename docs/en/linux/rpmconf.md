---
layout: page
title: linux/rpmconf (English)
description: "Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades."
content_hash: 3973ec668a28ac027c55cdcf2dfdf7afa5dde803
last_modified_at: 2024-01-26
tldri18n_status: 2
---
# rpmconf

Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades.
See also: `rpm`.
More information: <https://github.com/xsuchy/rpmconf>.

- List leftover files and interactively choose what to do with each of them:

`sudo rpmconf --all`

- Delete orphaned RPMNEW and RPMSAVE files:

`sudo rpmconf --all --clean`
