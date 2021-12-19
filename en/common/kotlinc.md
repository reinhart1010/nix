---
layout: page
title: common/kotlinc (English)
description: "Kotlin compiler."
content_hash: fa1b9580631766833142caf63300eb31ead6982c
---
# kotlinc

Kotlin compiler.
More information: <https://kotlinlang.org/docs/command-line.html>.

- Start a REPL (interactive shell):

`kotlinc`

- Compile a Kotlin file:

`kotlinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.kt</span>

- Compile several Kotlin files:

`kotlinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.kt path/to/file2.kt ...</span>

- Execute a specific Kotlin Script file:

`kotlinc -script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.kts</span>

- Compile a Kotlin file into a self contained jar file with the Kotlin runtime library included:

`kotlinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.kt</span>` -include-runtime -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>
