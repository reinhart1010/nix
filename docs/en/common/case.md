---
layout: page
title: common/case (English)
description: "Bash builtin construct for creating multi-choice conditional statements."
content_hash: 9e3c60cdc299d50be45d24c9a04a54bbad0b8d18
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/case.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/case.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/case.html
    icon: bi bi-globe
tldri18n_status: 2
---
# case

Bash builtin construct for creating multi-choice conditional statements.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- Match a variable against string literals to decide which command to run:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$tocount</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">words</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w README</span>`; ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lines</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l README</span>`; ;; esac`

- Combine patterns with |, use * as a fallback pattern:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$tocount</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[wW]|words</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w README</span>`; ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[lL]|lines</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l README</span>`; ;; *) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "what?"</span>`; ;; esac`
