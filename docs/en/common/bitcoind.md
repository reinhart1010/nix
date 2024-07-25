---
layout: page
title: common/bitcoind (English)
description: "Bitcoin Core daemon."
content_hash: f1cf9be2704dbc7a9a07a5bae27f120a107986a9
last_modified_at: 2024-07-25
tldri18n_status: 2
---
# bitcoind

Bitcoin Core daemon.
Uses the configuration defined in `bitcoin.conf`.
More information: <https://manned.org/bitcoind>.

- Start the Bitcoin Core daemon (in the foreground):

`bitcoind`

- Start the Bitcoin Core daemon in the background (use `bitcoin-cli stop` to stop):

`bitcoind -daemon`

- Start the Bitcoin Core daemon on a specific network:

`bitcoind -chain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|test|signet|regtest</span>

- Start the Bitcoin Core daemon using specific config file and data directory:

`bitcoind -conf=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bitcoin.conf</span>` -datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
