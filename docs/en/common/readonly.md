---
layout: page
title: common/readonly (English)
description: "Create or modify read-only variables within a shell script, preventing the variable from being changed by subsequent commands."
content_hash: 3f4b78c21dd80c5ee302625f069aa4581ce55d19
last_modified_at: 2023-10-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># readonly

Create or modify read-only variables within a shell script, preventing the variable from being changed by subsequent commands.
This is useful when you want to ensure that a variable retains a constant value throughout the execution of a script.
More information: <https://manned.org/readonly.1p>.

- Create a read-only variable:

`readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Mark a variable as read-only:

`readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">existing_variable</span>

- [p]rint to the standard output the names and values of all read-only variables:

`readonly -p`
