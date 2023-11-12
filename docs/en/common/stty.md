---
layout: page
title: common/stty (English)
description: "Set options for a terminal device interface."
content_hash: 2e01331d5666a9ae16b48dfaa505fc42359d738b
last_modified_at: 2023-11-12
related_topics:
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
More information: <https://www.gnu.org/software/coreutils/stty>.

- Display all settings for the current terminal:

`stty --all`

- Set the number of rows or columns:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Get the actual transfer speed of a device:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` speed`

- Reset all modes to reasonable values for the current terminal:

`stty sane`
