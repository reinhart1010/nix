---
layout: page
title: linux/libtoolize (English)
description: "An `autotools` tool to prepare a package for using `libtool`."
content_hash: abb1978eda4f09458a0da692305182c2a2e52192
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# libtoolize

An `autotools` tool to prepare a package for using `libtool`.
It performs various tasks, including generating necessary files and directories to integrate `libtool` seamlessly into a project.
More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialize a project for `libtool` by copying necessary files (avoiding symbolic links) and overwriting existing files if needed:

`libtoolize --copy --force`
