---
layout: page
title: common/iverilog (English)
description: "Preprocesses and compiles Verilog HDL (IEEE-1364) code, into executable programs for simulation."
content_hash: 15500ebbb86b45b78c3fa1c0172eb5f38afb4e7f
---
# iverilog

Preprocesses and compiles Verilog HDL (IEEE-1364) code, into executable programs for simulation.
More information: <http://iverilog.icarus.com/>.

- Compile a source file into an executable:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.v</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>

- Also display all warnings:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.v</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>

- Compile and run explicitly using the VVP runtime:

`iverilog -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` -tvvp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.v</span>

- Compile using Verilog library files from a different path:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.v</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library_directory</span>

- Preprocess Verilog code without compiling:

`iverilog -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.v</span>
