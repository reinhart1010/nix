---
layout: page
title: common/jbang (English)
description: "Easily create, edit and run self-contained source-only Java programs."
content_hash: 83060ca07a4fa410b019a23342503078e5955529
last_modified_at: 2024-01-11
tldri18n_status: 2
---
# jbang

Easily create, edit and run self-contained source-only Java programs.
See also: `java`.
More information: <https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>.

- Initialize a simple Java class:

`jbang init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.java</span>

- Initialize a Java class (useful for scripting):

`jbang init --template=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.java</span>

- Use `jshell` to explore and use a script and any dependencies in a REPL editor:

`jbang run --interactive`

- Setup a temporary project to edit a script in an IDE:

`jbang edit --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codium|code|eclipse|idea|netbeans|gitpod</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.java</span>

- Run a Java code snippet (Java 9 and later):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'</span>` | jbang -`

- Run command line application:

`jbang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>

- Install a script on the user's `$PATH`:

`jbang app install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.java</span>

- Install a specific version of JDK to be used with `jbang`:

`jbang jdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
