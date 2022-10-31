---
layout: page
title: common/javap (English)
description: "Disassemble one or more class files and list them."
content_hash: 61186b3c60b47aa1920806ab6e2d3445ee1c901c
---
# javap

Disassemble one or more class files and list them.
More information: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/javap.html>.

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
