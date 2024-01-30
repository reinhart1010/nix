---
layout: page
title: common/makensis (English)
description: "Cross-platform compiler for NSIS installers."
content_hash: 6e1fe20d6962047666309e8ccfa05b3871636689
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# makensis

Cross-platform compiler for NSIS installers.
It compiles a NSIS script into a Windows installer executable.
More information: <https://nsis.sourceforge.io/Docs/Chapter3.html>.

- Compile a NSIS script:

`makensis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nsi</span>

- Compile a NSIS script in strict mode (treat warnings as errors):

`makensis -WX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nsi</span>

- Display help for a specific command:

`makensis -CMDHELP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
