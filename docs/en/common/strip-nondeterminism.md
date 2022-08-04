---
layout: page
title: common/strip-nondeterminism (English)
description: "A tool to remove non-deterministic information (e.g. timestamps) from files."
content_hash: cc19e7b3f8376ea7e5d9d14700daf19e62d44e0a
---
# strip-nondeterminism

A tool to remove non-deterministic information (e.g. timestamps) from files.
More information: <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>.

- Strip nondeterministic information from a file:

`strip-nondeterminism `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Strip nondeterministic information from a file manually specifying the filetype:

`strip-nondeterminism --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filetype</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Strip nondeterministic information from a file; instead of removing timestamps set them to the specified UNIX timestamp:

`strip-nondeterminism --timestamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unix_timestamp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
