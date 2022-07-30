---
layout: page
title: common/pkg-config (English)
description: "Provide the details of installed libraries for compiling applications."
content_hash: 92b053035b839fe55deba1c3a7774a56c4d5040d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkg-config

Provide the details of installed libraries for compiling applications.
More information: <https://www.freedesktop.org/wiki/Software/pkg-config/>.

- Get the list of libraries and their dependencies:

`pkg-config --libs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library1 library2 ...</span>

- Get the list of libraries, their dependencies, and proper cflags for gcc:

`pkg-config --cflags --libs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library1 library2 ...</span>

- Compile your code with libgtk-3, libwebkit2gtk-4.0 and all their dependencies:

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`
