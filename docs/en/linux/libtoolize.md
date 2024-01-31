---
layout: page
title: linux/libtoolize (English)
description: "A tool used in the autotools build system to prepare a package for using `libtool`."
content_hash: 3709b62e671e3b573cfec0c214e24fffe55b820d
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# libtoolize

A tool used in the autotools build system to prepare a package for using `libtool`.
It performs various tasks, including generating necessary files and directories to integrate `libtool` seamlessly into a project.
More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialize a project for `libtool` by copying necessary files (avoiding symbolic links) and overwriting existing files if needed:

`libtoolize --copy --force`
