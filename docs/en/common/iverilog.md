---
layout: page
title: common/iverilog (English)
description: "Preprocesses and compiles Verilog HDL (IEEE-1364) code into executable programs for simulation."
content_hash: e9dcfcc978dcf8ea1da534b3196834caa48cb149
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/common/iverilog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iverilog

Preprocesses and compiles Verilog HDL (IEEE-1364) code into executable programs for simulation.
More information: <https://github.com/steveicarus/iverilog>.

- Compile a source file into an executable:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Compile a source file into an executable while displaying all warnings:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Compile and run explicitly using the VVP runtime:

`iverilog -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` -tvvp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>

- Compile using Verilog library files from a different path:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library_directory</span>

- Preprocess Verilog code without compiling:

`iverilog -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>
