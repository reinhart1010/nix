---
layout: page
title: common/rekor-cli (English)
description: "Immutable tamper resistant ledger of metadata generated within a software projects supply chain."
content_hash: 787b202fb944764db35fdd164c03ce9d3e199c3e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rekor-cli

Immutable tamper resistant ledger of metadata generated within a software projects supply chain.
More information: <https://github.com/sigstore/rekor>.

- Upload an artifact to Rekor:

`rekor-cli upload --artifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext</span>` --signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext.sig</span>` --pki-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x509</span>` --public-key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.pub</span>

- Get information regarding entries in the Transparency Log:

`rekor-cli get --uuid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1</span>

- Search the Rekor index to find entries by Artifact:

`rekor-cli search --artifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext</span>

- Search the Rekor index to find entries by a specific hash:

`rekor-cli search --sha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b</span>
