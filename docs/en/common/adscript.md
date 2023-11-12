---
layout: page
title: common/adscript (English)
description: "Compiler for Adscript files."
content_hash: 273c162ce76f1d1d77c2cf1882727022d3c42ff0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/adscript.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adscript.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adscript.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adscript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adscript

Compiler for Adscript files.
More information: <https://github.com/Amplus2/Adscript>.

- Compile a file to an object file:

`adscript --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.adscript</span>

- Compile and link a file to a standalone executable:

`adscript --executable --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.adscript</span>

- Compile a file to LLVM IR instead of native machine code:

`adscript --llvm-ir --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.adscript</span>

- Cross-compile a file to an object file for a foreign CPU architecture or operating system:

`adscript --target-triple `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-linux-elf</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.adscript</span>
