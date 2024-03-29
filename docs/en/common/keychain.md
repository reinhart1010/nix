---
layout: page
title: common/keychain (English)
description: "Re-use ssh-agent and/or gpg-agent between logins."
content_hash: 1db0fff0c6ee918ba89c39d1a00cef9447cd8f19
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# keychain

Re-use ssh-agent and/or gpg-agent between logins.
More information: <http://funtoo.org/Keychain>.

- Check for a running ssh-agent, and start one if needed:

`keychain`

- Also check for gpg-agent:

`keychain --agents "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg,ssh</span>`"`

- List signatures of all active keys:

`keychain --list`

- List fingerprints of all active keys:

`keychain --list-fp`

- Add a timeout for identities added to the agent, in minutes:

`keychain --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>
