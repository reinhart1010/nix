---
layout: page
title: linux/hlint (English)
description: "Suggest improvements to Haskell code."
content_hash: 79aeeafacdd1e599d65657236f8b0babf2a12484
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# hlint

Suggest improvements to Haskell code.
More information: <https://hackage.haskell.org/package/hlint>.

- Display suggestions for a given file:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` options`

- Check all Haskell files and generate a report:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --report`

- Automatically apply most suggestions:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --refactor`

- Display additional options:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --refactor-options`

- Generate a settings file ignoring all outstanding hints:

`hlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --default > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.hlint.yaml</span>
