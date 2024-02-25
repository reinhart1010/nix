---
layout: page
title: common/tokei (English)
description: "Display statistics about code."
content_hash: d3f3ffc88f3382e97bc1f20eb57a45127fa5d7b1
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# tokei

Display statistics about code.
More information: <https://github.com/XAMPPRocky/tokei>.

- Display a report for the code in a directory and all subdirectories:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display a report for a directory excluding `.min.js` files:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.min.js</span>

- Display statistics for individual files in a directory:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --files`

- Display a report for all files of type Rust and Markdown:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rust</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Markdown</span>
