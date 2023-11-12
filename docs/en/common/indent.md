---
layout: page
title: common/indent (English)
description: "Change the appearance of a C/C++ program by inserting or deleting whitespace."
content_hash: c33066354d16530cda223409c0c36c6952f05c0c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# indent

Change the appearance of a C/C++ program by inserting or deleting whitespace.
More information: <https://www.gnu.org/software/indent/>.

- Format C/C++ source according to the Linux style guide, automatically back up the original files, and replace with the indented versions:

`indent --linux-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/another_source.c</span>

- Format C/C++ source according to the GNU style, saving the indented version to a different file:

`indent --gnu-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/indented_source.c</span>

- Format C/C++ source according to the style of Kernighan & Ritchie (K&R), no tabs, 3 spaces per indent, and wrap lines at 120 characters:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/indented_source.c</span>
