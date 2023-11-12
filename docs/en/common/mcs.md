---
layout: page
title: common/mcs (English)
description: "Mono C# Compiler."
content_hash: f3ae14da928d04798e1d62b38eb25c22dd52e8dc
last_modified_at: 2023-11-12
related_topics:
  - title: русский version
    url: /ru/common/mcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mcs

Mono C# Compiler.
More information: <https://manned.org/mcs.1>.

- Compile the specified files:

`mcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file1.cs path/to/input_file2.cs ...</span>

- Specify the output program name:

`mcs -out:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file1.cs path/to/input_file2.cs ...</span>

- Specify the output program type:

`mcs -target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exe|winexe|library|module</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file1.cs path/to/input_file2.cs ...</span>
