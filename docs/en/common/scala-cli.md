---
layout: page
title: common/scala-cli (English)
description: "Interact with the Scala programming language."
content_hash: 9310b3d0ce423ea61160f4b1612a692d29a36fbf
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# scala-cli

Interact with the Scala programming language.
More information: <https://scala-cli.virtuslab.org/docs/overview/>.

- Start a REPL (interactive shell) using a specific Scala and JVM version:

`scala-cli --scala `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.1.0</span>` --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temurin:17</span>

- Compile and run a Scala script:

`scala-cli run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.scala</span>

- Compile and test a Scala script:

`scala-cli test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.scala</span>

- Format a Scala script, updating the file in-place:

`scala-cli fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.scala</span>

- Generate files for IDE (VSCode and IntelliJ) support:

`scala-cli setup-ide `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.scala</span>
