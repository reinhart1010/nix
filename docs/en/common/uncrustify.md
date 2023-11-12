---
layout: page
title: common/uncrustify (English)
description: "C, C++, C#, D, Java and Pawn source code formatter."
content_hash: 42b764fd35205418f674bb7448838cf65651d832
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# uncrustify

C, C++, C#, D, Java and Pawn source code formatter.
More information: <https://github.com/uncrustify/uncrustify>.

- Format a single file:

`uncrustify -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.cpp</span>

- Read filenames from `stdin`, and take backups before writing output back to the original filepaths:

`find . -name "*.cpp" | uncrustify -F - --replace`

- Don't make backups (useful if files are under version control):

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- Use a custom configuration file and write the result to `stdout`:

`uncrustify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/uncrustify.cfg</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Explicitly set a configuration variable's value:

`uncrustify --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Generate a new configuration file:

`uncrustify --update-config -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new.cfg</span>
