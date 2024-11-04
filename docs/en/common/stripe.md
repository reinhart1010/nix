---
layout: page
title: common/stripe (English)
description: "Interact with a Stripe account."
content_hash: 4a8aee4ecfa2767720608ddeeb2cc48c537bf522
last_modified_at: 2024-11-04
tldri18n_status: 2
---
# stripe

Interact with a Stripe account.
More information: <https://docs.stripe.com/stripe-cli>.

- Follow the logs of activity on the account:

`stripe logs tail`

- Listen for events, filtering on events with the name `charge.succeeded` and forwarding them to localhost:3000/events:

`stripe listen --events="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">charge.succeeded</span>`" --forward-to="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost:3000/events</span>`"`

- Send a test webhook event:

`stripe trigger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">charge.succeeded</span>

- Create a customer:

`stripe customers create --email="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test@example.com</span>`" --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Jenny Rosen</span>`"`

- Print to JSON:

`stripe listen --print-json`
