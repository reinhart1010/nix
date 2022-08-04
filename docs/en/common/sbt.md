---
layout: page
title: common/sbt (English)
description: "Build tool for Scala and Java projects."
content_hash: e9205de405b55eca269dcb8ff50914f4f82433bc
---
# sbt

Build tool for Scala and Java projects.
More information: <https://www.scala-sbt.org/1.x/docs/>.

- Start a REPL (interactive shell):

`sbt`

- Create a new Scala project from an existing Giter8 template hosted on GitHub:

`sbt new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scala/hello-world.g8</span>

- Compile and run all tests:

`sbt test`

- Delete all generated files in the `target` directory:

`sbt clean`

- Compile the main sources in `src/main/scala` and `src/main/java` directories:

`sbt compile`

- Use the specified version of sbt:

`sbt -sbt-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Use a specific jar file as the sbt launcher:

`sbt -sbt-jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- List all sbt options:

`sbt -h`
