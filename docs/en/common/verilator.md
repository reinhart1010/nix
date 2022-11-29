---
layout: page
title: common/verilator (English)
description: "Converts Verilog and SystemVerilog hardware description language (HDL) design into a C++ or SystemC model to be executed after compiling."
content_hash: a7135884bd85ff27e57fcc45896ffb2f0e295cee
last_modified_at: 2022-11-29
---
# verilator

Converts Verilog and SystemVerilog hardware description language (HDL) design into a C++ or SystemC model to be executed after compiling.
More information: <https://veripool.org/guide/latest/>.

- Build a specific C project in the current directory:

`verilator --binary --build-jobs 0 -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.v</span>

- Create a C++ executable in a specific folder:

`verilator --cc --exe --build --build-jobs 0 -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.cpp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.v</span>

- Perform linting over a code in the current directory:

`verilator --lint-only -Wall`

- Create XML output about the design (files, modules, instance hierarchy, logic and data types) to feed into other tools:

`verilator --xml-output -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>
