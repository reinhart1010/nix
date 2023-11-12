---
layout: page
title: windows/pabcnetcclear (English)
description: "Preprocess and compile PascalABC.NET source files."
content_hash: 724ea6d43dc6c4cd1e0fe42def78f6f96da33469
last_modified_at: 2023-11-12
related_topics:
  - title: русский version
    url: /ru/windows/pabcnetcclear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pabcnetcclear

Preprocess and compile PascalABC.NET source files.
More information: <http://pascalabc.net>.

- Compile the specified source file into an executable with the same name:

`pabcnetcclear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file.pas</span>

- Compile the specified source file into an executable with the specified name:

`pabcnetcclear /Output:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\_file.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file.pas</span>

- Compile the specified source file into an executable with the same name along with/without debug information:

`pabcnetcclear /Debug:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file.pas</span>

- Allow units to be searched in the specified path while compiling the source file into an executable with the same name:

`pabcnetcclear /SearchDir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file.pas</span>

- Compile the specified source file into an executable, defining a symbol:

`pabcnetcclear /Define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">symbol</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file.pas</span>
