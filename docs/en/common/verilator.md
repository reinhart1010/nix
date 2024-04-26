---
layout: page
title: common/verilator (English)
description: "Convert Verilog and SystemVerilog hardware description language (HDL) design into a C++ or SystemC model to be executed after compiling."
content_hash: e5222b7a907ba2a7f17157961cab5b7578f8f5b6
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# verilator

Convert Verilog and SystemVerilog hardware description language (HDL) design into a C++ or SystemC model to be executed after compiling.
More information: <https://veripool.org/guide/latest/>.

- Build a specific C project in the current directory:

`verilator --binary --build-jobs 0 -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>

- Create a C++ executable in a specific folder:

`verilator --cc --exe --build --build-jobs 0 -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.cpp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.v</span>

- Perform linting over a code in the current directory:

`verilator --lint-only -Wall`

- Create XML output about the design (files, modules, instance hierarchy, logic and data types) to feed into other tools:

`verilator --xml-output -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>
