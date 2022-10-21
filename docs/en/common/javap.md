---
layout: page
title: common/javap (English)
description: "Disassemble one or more class files and list them."
content_hash: 7d31d7de8976f39cc7ed3fcf479e16ab53b96513
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># javap

Disassemble one or more class files and list them.
More information: <https://docs.oracle.com/en/java/javase/18/docs/specs/man/javap.html>.

- Disassemble and list a `.class` file:

`javap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.class</span>

- Disassemble and list multiple `.class` files:

`javap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.class path/to/file2.class ...</span>

- Disassemble and list a built-in class file:

`javap java.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class</span>

- Display help:

`javap -help`

- Display version:

`javap -version`
