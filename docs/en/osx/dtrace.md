---
layout: page
title: osx/dtrace (English)
description: "A simple interface to invoke the D language compiler, retrieve buffered trace, and print traced data from the DTrace kernel facility."
content_hash: 79166e4c15277ab8a3aef725350c1618467ce7fa
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# dtrace

A simple interface to invoke the D language compiler, retrieve buffered trace, and print traced data from the DTrace kernel facility.
Generic front-end to DTrace facility, requiring root privileges.
More information: <https://keith.github.io/xcode-man-pages/dtrace.1.html>.

- Set target data model for a specific architecture:

`dtrace -arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch_name</span>

- Claim [a]nonymous tracing state and display the traced data:

`dtrace -a`

- Set principal trace buffer size. Supported units are `k`, `m`, `g`, or `t`:

`dtrace -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2g</span>

- Compile the specified D Program [s]ource file:

`dtrace -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D_script</span>

- Run the specified [c]ommand and exit upon its completion:

`dtrace -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify [f]unction name to trace or list (-l option). The corresponding argument can include any of the probe description forms like `provider:module:function`, `module:function` or `function`:

`dtrace -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>

- Grad the specified [p]rocess ID, cache its symbol table, and exit upon completion:

`dtrace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Combine different options for tracing function in a process:

`dtrace -a -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buffer_size</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
