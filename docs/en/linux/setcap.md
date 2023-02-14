---
layout: page
title: linux/setcap (English)
description: "Set capabilities of specified file."
content_hash: 229747fc659922fd43c77bd2a2eed998418f5b7d
last_modified_at: 2023-02-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># setcap

Set capabilities of specified file.
See also: `tldr getcap`.
More information: <https://manned.org/setcap>.

- Set capability `cap_net_raw` (to use RAW and PACKET sockets) for a given file:

`setcap '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_raw</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set multiple capabilities on a file (ep behind the capability means "effective permitted"):

`setcap '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_dac_read_search,cap_sys_tty_config+ep</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove all capabilities from a file:

`setcap -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Verify that the specified capabilities are currently associated with the specified file:

`setcap -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_raw</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- The optional `-n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rootuid</span> argument can be used to set the file capability for use only in a user namespace with this root user ID owner:

`setcap -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rootuid</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_admin</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
