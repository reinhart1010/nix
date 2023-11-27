---
layout: page
title: common/sg (English)
description: "Ast-grep is a tool for code structural search, lint, and rewriting."
content_hash: 03acd7f185635086ee6faf3be9c363b9ce192366
last_modified_at: 2023-11-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sg

Ast-grep is a tool for code structural search, lint, and rewriting.
More information: <https://ast-grep.github.io/guide/introduction.html>.

- Scan for possible queries using interactive mode:

`sg scan --interactive`

- Rewrite code in the current directory using patterns:

`sg run --pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`' --rewrite '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>`' --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python</span>

- Visualize possible changes without applying them:

`sg run --pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">useState<number>($A)</span>`' --rewrite '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">useState($A)</span>`' --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">typescript</span>

- Output results as JSON, extract information using `jq` and interactively view it using `jless`:

`sg run --pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Some($A)</span>`' --rewrite '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">None</span>`' --json | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[].replacement</span>`' | jless`
