---
layout: page
title: linux/fprintd-delete (English)
description: "Remove fingerprints from the database."
content_hash: b7f56f35f8dd3dc6547ce7fae62397cc69ee5c73
---
# fprintd-delete

Remove fingerprints from the database.
More information: <https://manned.org/fprintd-delete>.

- Remove all fingerprints for a specific user:

`fprintd-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a specific fingerprints for a specific user:

`fprintd-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger</span>

- Display help:

`fprintd-delete`
