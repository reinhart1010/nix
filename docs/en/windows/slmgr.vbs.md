---
layout: page
title: windows/slmgr.vbs (English)
description: "Install, activate, and manage Windows licenses."
content_hash: bd3df6d8a72ff2ddc4130cb33760c51f3f25bd78
last_modified_at: 2023-12-02
related_topics:
  - title: Nederlands version
    url: /nl/windows/slmgr.vbs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slmgr.vbs

Install, activate, and manage Windows licenses.
This command may override, deactivate, and/or remove your current Windows license. Please proceed with caution.
More information: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- [d]isplay the current Windows [l]icense [i]nformation:

`slmgr.vbs /dli`

- [d]isplay the ins[t]allation [i]D for the current device. Useful for offline license activation:

`slmgr.vbs /dti`

- Display the current license's e[xp]i[r]ation date and time:

`slmgr.vbs /xpr`

- [i]nstall a new Windows license [p]roduct [k]ey. Requires Administrator privileges and will override the existing license:

`slmgr.vbs /ipk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_key</span>

- [a]c[t]ivate the Windows product license [o]nline. Requires Administrator privileges to do so:

`slmgr.vbs /ato`

- [a]c[t]ivate the Windows [p]roduct license offline. Requires Administrator privileges and an Confirmation ID provided by Microsoft Product Activation Center:

`slmgr.vbs /atp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmation_id</span>

- [c]lear the current license's [p]roduct [k]e[y] from the Windows Registry. This will not deactivate or uninstall the current license, but prevents the key from being stolen by malicious programs in the future:

`slmgr.vbs /cpky`

- [u]ninstall the current license (by its [p]roduct [k]ey):

`slmgr.vbs /upk`
