---
layout: page
title: linux/vkpurge (English)
description: "List or remove old kernel versions left behind by `xbps`."
content_hash: 70d194dce979b85d453058d4e0f24d4ca58cc4b7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vkpurge

List or remove old kernel versions left behind by `xbps`.
The `version` arguments support shell globs.
More information: <https://man.voidlinux.org/vkpurge.8>.

- List all removable kernel versions (or those matching `version` if the argument is specified):

`vkpurge list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Remove all unused kernels:

`vkpurge rm all`

- Remove kernel versions matching `version`:

`vkpurge rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
