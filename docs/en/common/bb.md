---
layout: page
title: common/bb (English)
description: "Native Clojure interpreter for scripting."
content_hash: ff00c173e8e6f7281238ff6bfb2e34f38d214374
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bb

Native Clojure interpreter for scripting.
More information: <https://book.babashka.org/#usage>.

- [e]valuate an expression:

`bb -e "(+ 1 2 3)"`

- Evaluate a script [f]ile:

`bb -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.clj</span>

- Bind input to a sequence of lines from stdin:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Bind input to a sequence of EDN(Extensible Data Notation) values from stdin:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
