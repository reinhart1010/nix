---
layout: page
title: windows/slmgr.vbs (English)
description: "Install, activate, and manage Windows licenses."
content_hash: 0bc7e7796723e10aed55032d5977b6aa06dc9271
last_modified_at: 2023-07-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># slmgr.vbs

Install, activate, and manage Windows licenses.
This command may override, deactivate, and/or remove your current Windows license. Please proceed with caution.
More information: <https://docs.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- [d]isplay the current Windows [l]icense [i]nformation:

`slmgr /dli`

- [d]isplay the ins[t]allation [i]D for the current device. Useful for offline license activation:

`slmgr /dti`

- Display the current license's e[xp]i[r]ation date and time:

`slmgr /xpr`

- [i]nstall a new Windows license [p]roduct [k]ey. Requires Administrator privileges and will override the existing license:

`slmgr /ipk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_key</span>

- [a]c[t]ivate the Windows product license [o]nline. Requires Administrator privileges to do so:

`slmgr /ato`

- [a]c[t]ivate the Windows [p]roduct license offline. Requires Administrator privileges and an Confirmation ID provided by Microsoft Product Activation Center:

`slmgr /atp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmation_id</span>

- [c]lear the current license's [p]roduct [k]e[y] from the Windows Registry. This will not deactivate or uninstall the current license, but prevents the key from being stolen by malicious programs in the future:

`slmgr /cpky`

- [u]ninstall the current license (by its [p]roduct [k]ey):

`slmgr /upk`
