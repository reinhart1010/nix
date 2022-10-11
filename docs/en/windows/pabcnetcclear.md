---
layout: page
title: windows/pabcnetcclear (English)
description: "Preprocess and compile PascalABC.NET source files."
content_hash: f98d80efaa9e74cc8112132688551f8aea846dee
related_topics:
  - title: русский version
    url: /ru/windows/pabcnetcclear.html
    icon: bi bi-globe
---
# pabcnetcclear

Preprocess and compile PascalABC.NET source files.
More information: <http://pascalabc.net>.

- Compile the specified source file into an executable with the same name:

`pabcnetcclear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.pas</span>

- Compile the specified source file into an executable with the specified name:

`pabcnetcclear /Output:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.pas</span>

- Compile the specified source file into an executable with the same name along with/without debug information:

`pabcnetcclear /Debug:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.pas</span>

- Allow units to be searched in the specified path while compiling the source file into an executable with the same name:

`pabcnetcclear /SearchDir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.pas</span>

- Compile the specified source file into an executable, defining a symbol:

`pabcnetcclear /Define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">symbol</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.pas</span>
