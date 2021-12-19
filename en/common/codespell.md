---
layout: page
title: common/codespell (English)
description: "Spellchecker for source code."
content_hash: bbfef373a25d2ab8c1378114347f608fc9358445
---
# codespell

Spellchecker for source code.
More information: <https://github.com/codespell-project/codespell>.

- Check for typos in all text files in the current directory, recursively:

`codespell`

- Correct all typos found in-place:

`codespell --write-changes`

- Skip files with names that match the specified pattern (accepts a comma-separated list of patterns using wildcards):

`codespell --skip "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Use a custom dictionary file when checking (`--dictionary` can be used multiple times):

`codespell --dictionary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Do not check words that are listed in the specified file:

`codespell --ignore-words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Do not check the specified words:

`codespell --ignore-words-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">words,to,ignore</span>

- Print 3 lines of context around, before or after each match:

`codespell --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Check file names for typos, in addition to file contents:

`codespell --check-filenames`
