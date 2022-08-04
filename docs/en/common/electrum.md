---
layout: page
title: common/electrum (English)
description: "Ergonomic Bitcoin wallet and private key management."
content_hash: 5e52ea1d50b981822f47a2ecf464cdd8785b7722
related_topics:
  - title: italiano version
    url: /it/common/electrum.html
    icon: bi bi-globe
---
# electrum

Ergonomic Bitcoin wallet and private key management.
More information: <https://electrum.org>.

- Create a new wallet:

`electrum -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_wallet.dat</span>` create`

- Restore an existing wallet from seed offline:

`electrum -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recovery_wallet.dat</span>` restore -o`

- Create a signed transaction offline:

`electrum mktx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amount</span>` -f 0.0000001 -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from</span>` -o`

- Display all wallet receiving addresses:

`electrum listaddresses -a`

- Sign a message:

`electrum signmessage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Verify a message:

`electrum verifymessage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">signature</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Connect only to a specific electrum-server instance:

`electrum -p socks5:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>`:9050 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">56ckl5obj37gypcu.onion</span>`:50001:t -1`
