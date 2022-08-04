---
layout: page
title: linux/chntpw (English)
description: "A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM."
content_hash: b0ca9becaa5273c3dff8a50551a8931deda7ba04
---
# chntpw

A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.
Boot target machine with live cd like Kali Linux and run with elevated privileges.
More information: <http://pogostick.net/~pnh/ntpasswd>.

- List all users in the SAM file:

`chntpw -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sam_file</span>

- Edit [u]ser interactively:

`chntpw -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sam_file</span>

- Use chntpw [i]nteractively:

`chntpw -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sam_file</span>
