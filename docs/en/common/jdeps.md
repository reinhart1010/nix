---
layout: page
title: common/jdeps (English)
description: "Java class dependency analyzer."
content_hash: 519e6ade90922375799c6d1d7edb47cad0457f9a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# jdeps

Java class dependency analyzer.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jdeps.html>.

- Analyze the dependencies of a `.jar` or `.class` file:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.class</span>

- Print a summary of all dependencies of a specific `.jar` file:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.jar</span>` -summary`

- Print all class-level dependencies of a `.jar` file:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.jar</span>` -verbose`

- Output the results of the analysis in a DOT file into a specific directory:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.jar</span>` -dotoutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display help:

`jdeps --help`
