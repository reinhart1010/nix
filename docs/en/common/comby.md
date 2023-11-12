---
layout: page
title: common/comby (English)
description: "Tool for structural code search and replace that supports many languages."
content_hash: b61e094e9d96530cb05bcceda00f3b7070c17973
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# comby

Tool for structural code search and replace that supports many languages.
More information: <https://github.com/comby-tools/comby>.

- Match and rewrite templates, and print changes:

`comby '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[a], :[b])</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[b], :[a])</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.rs</span>

- Match and rewrite with rewrite properties:

`comby '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[a], :[b])</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[b].Capitalize, :[a])</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.rs</span>

- Match and rewrite in-place:

`comby -in-place '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">match_pattern</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rewrite_pattern</span>`'`

- Only perform matching and print matches:

`comby -match-only '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">match_pattern</span>`' ""`
