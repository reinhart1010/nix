---
layout: page
title: common/vault (English)
description: "Interact with HashiCorp Vault."
content_hash: 6a2bfba01be78d71aedcb0be4721a6c84f65cf22
last_modified_at: 2023-07-16
---
# vault

Interact with HashiCorp Vault.
More information: <https://www.vaultproject.io/docs/commands>.

- Connect to a Vault server and initialize a new encrypted data store:

`vault init`

- Unseal (unlock) the vault, by providing one of the key shares needed to access the encrypted data store:

`vault unseal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key-share-x</span>

- Authenticate the CLI client against the Vault server, using an authentication token:

`vault auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authentication_token</span>

- Store a new secret in the vault, using the generic back-end called "secret":

`vault write secret/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello</span>` value=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">world</span>

- Read a value from the vault, using the generic back-end called "secret":

`vault read secret/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello</span>

- Read a specific field from the value:

`vault read -field=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>` secret/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello</span>

- Seal (lock) the Vault server, by removing the encryption key of the data store from memory:

`vault seal`
