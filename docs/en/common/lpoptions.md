---
layout: page
title: common/lpoptions (English)
description: "Display or set printer options and defaults."
content_hash: af02405d688c006e5ec43da7ea8283642711c99a
last_modified_at: 2023-12-18
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/lpoptions.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpoptions

Display or set printer options and defaults.
See also: `lpadmin`.
More information: <https://www.cups.org/doc/man-lpoptions.html>.

- Set the default printer:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer[/instance]</span>

- List printer-specific options of a specific printer:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -l`

- Set a new option on a specific printer:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>

- Remove the options of a specific printer:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -x`
