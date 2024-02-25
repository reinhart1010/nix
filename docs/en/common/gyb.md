---
layout: page
title: common/gyb (English)
description: "Locally back up Gmail messages using Gmail's API over HTTPS."
content_hash: 757d51ff3541f9ac92a418a7b84ee8fcb2f83415
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# gyb

Locally back up Gmail messages using Gmail's API over HTTPS.
More information: <https://github.com/GAM-team/got-your-back>.

- Estimate the number and the size of all emails on your Gmail account:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action estimate`

- Backup a Gmail account to a specific directory:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action backup --local-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Backup only important or starred emails from a Gmail account to the default local folder:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is:important OR is:starred</span>`"`

- Restore from a local folder to a Gmail account:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action restore --local-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
