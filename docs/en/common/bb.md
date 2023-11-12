---
layout: page
title: common/bb (English)
description: "Native Clojure interpreter for scripting."
content_hash: 10f73d5d2c785165e2f446f5e4226f67b353a5ce
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# bb

Native Clojure interpreter for scripting.
More information: <https://book.babashka.org/#usage>.

- [e]valuate an expression:

`bb -e "(+ 1 2 3)"`

- Evaluate a script [f]ile:

`bb -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.clj</span>

- Bind input to a sequence of lines from `stdin`:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Bind input to a sequence of EDN(Extensible Data Notation) values from `stdin`:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
