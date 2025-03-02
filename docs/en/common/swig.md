---
layout: page
title: common/swig (English)
description: "Generate bindings between C/C++ code and various high level languages such as JavaScript, Python, C#, and more."
content_hash: 6156d665e4d66a8f4d95678b4242a4504aad1d2b
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# swig

Generate bindings between C/C++ code and various high level languages such as JavaScript, Python, C#, and more.
It uses special `.i` or `.swg` files to generate the bindings (C/C++ with SWIG directives, then outputs a C/C++ file that contains all the wrapper code needed to build an extension module.
More information: <https://www.swig.org>.

- Generate a binding between C++ and Python:

`swig -c++ -python -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_wrapper.cpp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/swig_file.i</span>

- Generate a binding between C++ and Go:

`swig -go -cgo -intgosize 64 -c++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/swig_file.i</span>

- Generate a binding between C and Java:

`swig -java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/swig_file.i</span>

- Generate a binding between C and Ruby and prefix the Ruby module with `foo::bar::`:

`swig -ruby -prefix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo::bar::</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/swig_file.i</span>
