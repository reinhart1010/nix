---
layout: page
title: linux/vgremove (English)
description: "Remove volume group(s) in LVM."
content_hash: 1997c0ee18341d829f1048ea9f24fe55469e738d
last_modified_at: 2024-11-15
tldri18n_status: 2
---
# vgremove

Remove volume group(s) in LVM.
More information: <https://manned.org/vgremove>.

- Remove a volume group with confirmation:

`vgremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>

- Forcefully remove a volume group without confirmation:

`vgremove --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>

- Set the debug level for detailed logging to level 2, (repeat `--debug` up to 6 times to increase the level):

`vgremove --debug --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>

- Use a specific config setting to override defaults:

`vgremove --config '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global/locking_type=1</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>

- Display help text for usage information:

`vgremove --help`
