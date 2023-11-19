---
layout: page
title: common/keepassxc-cli (English)
description: "Command-line interface for KeepassXC."
content_hash: 57c415c6666b5a40ad4938a65549888fd691cf07
last_modified_at: 2023-11-19
tldri18n_status: 2
---
# keepassxc-cli

Command-line interface for KeepassXC.
More information: <https://manned.org/keepassxc-cli>.

- Search entries:

`keepassxc-cli search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List the contents of a folder:

`keepassxc-cli ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory</span>

- Add an entry with an auto-generated password:

`keepassxc-cli add --generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_name</span>

- Delete an entry:

`keepassxc-cli rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_name</span>

- Copy an entry's password to the clipboard:

`keepassxc-cli clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_name</span>

- Copy a TOTP code to the clipboard:

`keepassxc-cli clip --totp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_name</span>

- Generate a passphrase with 7 words:

`keepassxc-cli diceware --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Generate a password with 16 printable ASCII characters:

`keepassxc-cli generate --lower --upper --numeric --special --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>
