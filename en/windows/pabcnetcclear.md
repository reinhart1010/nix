---
layout: page
title: windows/pabcnetcclear (English)
description: "Preprocess and compile PascalABC.NET source files."
content_hash: 8c2157c1a48dac6f6e9f6e0fab86138f8f6d7791
related_topics:
  - title: русский version
    url: /ru/windows/pabcnetcclear.html
    icon: bi bi-globe
---
# pabcnetcclear

Preprocess and compile PascalABC.NET source files.
More information: <http://pascalabc.net>.

- Compile a source file into an executable with the same name:

`pabcnetcclear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pas</span>

- Compile a source file into an executable with the same name along with or without debug info:

`pabcnetcclear /Debug:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pas</span>

- Allow units to be searched in a path while compiling a source file into an executable with the same name:

`pabcnetcclear /SearchDir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pas</span>
