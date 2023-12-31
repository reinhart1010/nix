---
layout: page
title: common/rlwrap (English)
description: "Add line editing, persistent history and prompt completion to a REPL command."
content_hash: 11129443c784f641b4bb43ee13b95061a73f2275
last_modified_at: 2023-12-31
tldri18n_status: 2
---
# rlwrap

Add line editing, persistent history and prompt completion to a REPL command.
More information: <https://github.com/hanslub42/rlwrap>.

- Run a REPL command with line editing, persistent history and prompt completion:

`rlwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Use all words seen on input and output for prompt completion:

`rlwrap --remember `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Better prompt completion if prompts contain ANSI colour codes:

`rlwrap --ansi-colour-aware `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Enable filename completion (case sensitive):

`rlwrap --complete-filenames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Add coloured prompts, use colour name, or an ASCI-conformant colour specification. Use an uppercase colour name for bold styling:

`rlwrap --prompt-colour=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|red|green|yellow|blue|cyan|purple|white|colour_spec</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
