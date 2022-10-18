---
layout: page
title: common/gyb (English)
description: "Command line tool for locally backing up Gmail messages using Gmail's API over HTTPS."
content_hash: 38742fcc500fc6fe7d6b3b06fe33fa0b25583a0e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gyb

Command line tool for locally backing up Gmail messages using Gmail's API over HTTPS.
More information: <https://github.com/GAM-team/got-your-back>.

- Estimate the number and the size of all emails on your Gmail account:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action estimate`

- Backup a Gmail account to a specific directory:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action backup --local-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Backup only important or starred emails from a Gmail account to the default local folder:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is:important OR is:starred</span>`"`

- Restore from a local folder to a Gmail account:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action restore --local-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
