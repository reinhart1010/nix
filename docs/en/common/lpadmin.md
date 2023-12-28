---
layout: page
title: common/lpadmin (English)
description: "Configure CUPS printers and classes."
content_hash: 34c2291bb579b6ba5acb3fd89b3e5d974a3a169a
last_modified_at: 2023-12-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/lpadmin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpadmin

Configure CUPS printers and classes.
See also: `lpoptions`.
More information: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

- Set the default printer:

`lpadmin -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>

- Delete a specific printer or class:

`lpadmin -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer|class</span>

- Add a printer to a class:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class</span>

- Remove a printer from a class:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class</span>
