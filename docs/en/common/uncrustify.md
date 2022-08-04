---
layout: page
title: common/uncrustify (English)
description: "C, C++, C#, D, Java and Pawn source code formatter."
content_hash: 8ad1c2d2caf6e95c138ddf627235aab357203731
---
# uncrustify

C, C++, C#, D, Java and Pawn source code formatter.
More information: <https://github.com/uncrustify/uncrustify>.

- Format a single file:

`uncrustify -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.cpp</span>

- Read filenames from stdin, and take backups before writing output back to the original filepaths:

`find . -name "*.cpp" | uncrustify -F - --replace`

- Don't make backups (useful if files are under version control):

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- Use a custom configuration file and write the result to stdout:

`uncrustify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/uncrustify.cfg</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Explicitly set a configuration variable's value:

`uncrustify --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Generate a new configuration file:

`uncrustify --update-config -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new.cfg</span>
