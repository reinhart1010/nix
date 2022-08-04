---
layout: page
title: common/lpass (English)
description: "Command-line interface for the LastPass password manager."
content_hash: b84a80ec965022a1c5968492c30366717abfbced
---
# lpass

Command-line interface for the LastPass password manager.
More information: <https://github.com/lastpass/lastpass-cli>.

- Log in to your LastPass account, by entering your master password when prompted:

`lpass login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Show login status:

`lpass status`

- List all sites grouped by category:

`lpass ls`

- Generate a new password for gmail.com with the identifier `myinbox` and add to LastPass:

`lpass generate --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gmail.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myinbox</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_length</span>

- Show password for a specified entry:

`lpass show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myinbox</span>` --password`
