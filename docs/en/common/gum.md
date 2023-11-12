---
layout: page
title: common/gum (English)
description: "A tool for making glamorous shell scripts."
content_hash: 7fa19dbfae7556588a10172e6a60c1ee9b800e3b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gum

A tool for making glamorous shell scripts.
More information: <https://github.com/charmbracelet/gum>.

- Interactively pick a specific option to print to `stdout`:

`gum choose "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_2</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_3</span>`"`

- Open an interactive prompt for the user to input a string with a specific placeholder:

`gum input --placeholder "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Open an interactive confirmation prompt and exit with either `0` or `1`:

`gum confirm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Continue?</span>`" --default=false --affirmative "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Yes</span>`" --negative "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">No</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&& echo "Yes selected" || echo "No selected"</span>

- Show a spinner while a command is taking place with text alongside:

`gum spin --spinner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loading...</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Format text to include emojis:

`gum format -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emoji</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:smile: :heart: hello</span>`"`

- Interactively prompt for multi-line text (CTRL + D to save) and write to `data.txt`:

`gum write > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>
