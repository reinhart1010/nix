---
layout: page
title: common/gprbuild (English)
description: "A high-level build tool for projects written in Ada and other languages (C/C++/Fortran)."
content_hash: 6411bfa2236e5ed6ceef0d75fb83438f90bf7db8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gprbuild

A high-level build tool for projects written in Ada and other languages (C/C++/Fortran).
More information: <https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>.

- Build a project (assuming only one `*.gpr` file exists in the current directory):

`gprbuild`

- Build a specific [P]roject file:

`gprbuild -P`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Clean up the build workspace:

`gprclean`

- Install compiled binaries:

`gprinstall --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/installation/dir</span>
