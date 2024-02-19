---
layout: page
title: common/bb (English)
description: "Native Clojure interpreter for scripting."
content_hash: 987114c902a3287af9f8c46e696b4117d2c95161
last_modified_at: 2024-02-19
related_topics:
  - title: 한국어 version
    url: /ko/common/bb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bb

Native Clojure interpreter for scripting.
More information: <https://book.babashka.org/#usage>.

- [e]valuate an expression:

`bb -e "(+ 1 2 3)"`

- Evaluate a script [f]ile:

`bb -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.clj</span>

- Bind [i]nput to a sequence of lines from `stdin`:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Bind [I]nput to a sequence of EDN (Extensible Data Notation) values from `stdin`:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
