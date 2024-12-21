---
layout: page
title: osx/bclm (English)
description: "Set a custom charge limit on MacBooks."
content_hash: 2313956d71cdec9f2f753fd8b6dd2f99a6e45a6e
last_modified_at: 2024-12-21
tldri18n_status: 2
---
# bclm

Set a custom charge limit on MacBooks.
More information: <https://github.com/zackelia/bclme>.

- Set the charge limit to about 80% (for Intel machines, the battery charge level may be slightly lower than the set value):

`sudo bclm write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">77</span>

- Read the current charge limit:

`bclm read`

- Keep the charge limit after rebooting/smc reset:

`sudo bclm persist`

- Remove the persistent charge limit:

`sudo bclm unpersist`
