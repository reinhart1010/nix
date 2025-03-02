---
layout: page
title: common/filecheck (English)
description: "Flexible pattern matching file verifier."
content_hash: 88b69721829e431865ca32f2daceb4e6ffe0527b
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/filecheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# FileCheck

Flexible pattern matching file verifier.
It is typically used from LLVM regression tests and forms a part of a `lit` test.
More information: <https://llvm.org/docs/CommandGuide/FileCheck.html>.

- Match `input_file` content with pattern file `check_file`:

`FileCheck --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/check_file</span>

- Match input from the `stdin` with pattern file `check_file`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_text</span>`" | FileCheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/check_file</span>

- Match with the specified custom check `prefix` (Note: the default prefix is `CHECK`):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_text</span>`" | FileCheck --check-prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/check_file</span>

- Print good directive pattern matches:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_text</span>`" | FileCheck -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/check_file</span>

- Input `llvm_code.ll` into llvm-as, then pipe the output into FileCheck to match:

`llvm-as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/llvm_code.ll</span>` | FileCheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/check_file</span>
