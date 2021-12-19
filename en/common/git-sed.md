---
layout: page
title: common/git-sed (English)
description: "Replace patterns in git-controlled files using sed."
content_hash: 82d0d4fbd958f734519f952d71507a80957c643e
---
# git sed

Replace patterns in git-controlled files using sed.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>.

- Replace the specified text in the current repository:

`git sed '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_text</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_text</span>`'`

- Replace the specified text and then commit the resulting changes with a standard commit message:

`git sed -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_text</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_text</span>`'`

- Replace the specified text, using regular expressions:

`git sed -f g '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_text</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_text</span>`'`

- Replace a specific text in all files under a given directory:

`git sed '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_text</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_text</span>`' -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
