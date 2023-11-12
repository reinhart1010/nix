---
layout: page
title: common/tlmgr-pinning (English)
description: "The pinning action manages the pinning file."
content_hash: 45affa6a59481097ffdde3c90076195271c609b9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr pinning

The pinning action manages the pinning file.
More information: <https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

- Show the current pinning data:

`tlmgr pinning show`

- Pin the matching the packages to the given repository:

`tlmgr pinning add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove any packages recorded in the pinning file matching the packages for the given repository:

`tlmgr pinning remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove all pinning data for the given repository:

`tlmgr pinning remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --all`
