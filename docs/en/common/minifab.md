---
layout: page
title: common/minifab (English)
description: "Automate the setup and deployment of Hyperledger Fabric networks."
content_hash: 302719e05dfe3b525402d886f8d93a0b3af31da8
last_modified_at: 2024-02-25
related_topics:
  - title: italiano version
    url: /it/common/minifab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minifab

Automate the setup and deployment of Hyperledger Fabric networks.
More information: <https://github.com/hyperledger-labs/minifabric>.

- Bring up the default Hyperledger Fabric network:

`minifab up -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minifab_version</span>

- Bring down the Hyperledger Fabric network:

`minifab down`

- Install chaincode onto a specified channel:

`minifab install -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaincode_name</span>

- Install a specific chaincode version onto a channel:

`minifab install -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaincode_name</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaincode_version</span>

- Initialize the chaincode after installation/upgrade:

`minifab approve,commit,initialize,discover`

- Invoke a chaincode method with the specified arguments:

`minifab invoke -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaincode_name</span>` -p '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method_name</span>`", "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1</span>`", "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument2</span>`", ...'`

- Make a query on the ledger:

`minifab blockquery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">block_number</span>

- Quickly run an application:

`minifab apprun -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_programming_language</span>
