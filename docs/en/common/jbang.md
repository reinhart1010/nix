---
layout: page
title: common/jbang (English)
description: "Easily create, edit and run self-contained source-only Java programs."
content_hash: 83060ca07a4fa410b019a23342503078e5955529
last_modified_at: 2024-01-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jbang.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jbang

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
