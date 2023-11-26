---
layout: page
title: linux/libtoolize (English)
description: "A tool used in the autotools build system to prepare a package for the use of `libtool`."
content_hash: 581117df53920657eb70276fd530feb45c9df892
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# libtoolize

A tool used in the autotools build system to prepare a package for the use of `libtool`.
It performs various tasks, including generating necessary files and directories to integrate `libtool` seamlessly into a project.
More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialize a project for `libtool` by copying necessary files (avoiding symbolic links) and overwriting existing files if needed:

`libtoolize --copy --force`
