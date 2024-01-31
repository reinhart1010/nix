---
layout: page
title: common/javap (English)
description: "Disassemble class files and list them."
content_hash: d0a4826fcc489c2518ce72c97ad719a4f3212a29
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# javap

Disassemble class files and list them.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javap.html>.

- Disassemble and list one or more `.class` files:

`javap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.class path/to/file2.class ...</span>

- Disassemble and list a built-in class file:

`javap java.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class</span>

- Display help:

`javap -help`

- Display version:

`javap -version`
