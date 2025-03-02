---
layout: page
title: common/stty (English)
description: "Set options for a terminal device interface."
content_hash: 0b00fdd7984f48d348f5545f4dc95af5067c556e
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/stty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stty

Set options for a terminal device interface.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Display all settings for the current terminal:

`stty --all`

- Set the number of rows or columns:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Get the actual transfer speed of a device:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` speed`

- Reset all modes to reasonable values for the current terminal:

`stty sane`

- Switch between raw and normal mode:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw|cooked</span>

- Turn character echoing off or on:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-echo|echo</span>
