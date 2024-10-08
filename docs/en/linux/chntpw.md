---
layout: page
title: linux/chntpw (English)
description: "A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM."
content_hash: a71cf39fb1d799ebdf761b9d349f90a28197f77a
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# chntpw

A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.
Boot target machine with live cd like Kali Linux and run with elevated privileges.
More information: <https://pogostick.net/~pnh/ntpasswd>.

- List all users in the SAM file:

`chntpw -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sam_file</span>

- Edit user interactively:

`chntpw -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sam_file</span>

- Use chntpw interactively:

`chntpw -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sam_file</span>
