---
layout: page
title: common/dexdump (English)
description: "Display information about Android DEX files."
content_hash: 6ee7f692f154193ec036bf497db538a2a687776d
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/dexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dexdump

Display information about Android DEX files.
More information: <https://manned.org/dexdump>.

- Extract classes and methods from an APK file:

`dexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Display header information of DEX files contained in an APK file:

`dexdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Display the dis-assembled output of executable sections:

`dexdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Output results to a file:

`dexdump -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>
