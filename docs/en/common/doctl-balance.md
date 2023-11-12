---
layout: page
title: common/doctl-balance (English)
description: "Show the balance of a Digital Ocean account."
content_hash: 28aeb779b2fece51f81f13211dfe3dc0367f6742
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl balance

Show the balance of a Digital Ocean account.
More information: <https://docs.digitalocean.com/reference/doctl/reference/balance/>.

- Get balance of the account associated with the current context:

`doctl balance get`

- Get the balance of an account associated with an access token:

`doctl balance get --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Get the balance of an account associated with a specified context:

`doctl balance get --context`
