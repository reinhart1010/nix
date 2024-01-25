---
layout: page
title: common/vidir (English)
description: "Edit directories in a text editor."
content_hash: f88c22a837a45d34463ab16ea528ba5433e5b348
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# vidir

Edit directories in a text editor.
More information: <https://joeyh.name/code/moreutils/>.

- Edit the contents of the specified directories:

`vidir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Display each action taken by the program:

`vidir --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Edit the contents of current directory:

`vidir`

- Use the specified text editor:

`EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>` vidir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Read a list of files to edit from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | vidir -`
