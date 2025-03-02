---
layout: page
title: linux/dialog (English)
description: "Display dialog boxes on the terminal."
content_hash: 0cc26306240d2129ed39ce8a70db4b66dfaf9a4e
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/linux/dialog.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dialog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dialog

Display dialog boxes on the terminal.
More information: <https://manned.org/dialog>.

- Display a message:

`dialog --msgbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>

- Prompt the user for text:

`dialog --inputbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Enter text:</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>` 2>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>

- Prompt the user for a yes/no question:

`dialog --yesno "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Continue?</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>
