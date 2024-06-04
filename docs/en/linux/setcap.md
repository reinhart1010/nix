---
layout: page
title: linux/setcap (English)
description: "Set capabilities of specified file."
content_hash: ce40024b3f502ada599eefc9dccd55ed45550c0f
last_modified_at: 2024-06-04
tldri18n_status: 2
---
# setcap

Set capabilities of specified file.
See also: `getcap`.
More information: <https://manned.org/setcap>.

- Set capability `cap_net_raw` (to use RAW and PACKET sockets) for a given file:

`setcap '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_raw</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set multiple capabilities on a file (`ep` behind the capability means "effective permitted"):

`setcap '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_dac_read_search,cap_sys_tty_config+ep</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove all capabilities from a file:

`setcap -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Verify that the specified capabilities are currently associated with the specified file:

`setcap -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_raw</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- The optional `-n root_uid` argument can be used to set the file capability for use only in a user namespace with this root user ID owner:

`setcap -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_uid</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_admin</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
