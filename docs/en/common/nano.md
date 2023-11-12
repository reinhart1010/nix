---
layout: page
title: common/nano (English)
description: "Command-line text editor. An enhanced `Pico` clone."
content_hash: 1b6b001a7b7993c3e03f705a168bbb94005927e6
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/nano.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/nano.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nano.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nano.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nano

Command-line text editor. An enhanced `Pico` clone.
More information: <https://nano-editor.org>.

- Start the editor:

`nano`

- Start the editor without using configuration files:

`nano --ignorercfiles`

- Open specific files, moving to the next file when closing the previous one:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Open a file and position the cursor at a specific line and column:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file and enable soft wrapping:

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file and indent new lines to the previous line's indentation:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file and create a backup file (`path/to/file~`) on save:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
