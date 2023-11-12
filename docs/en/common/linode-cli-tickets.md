---
layout: page
title: common/linode-cli-tickets (English)
description: "Manage Linode Support Tickets."
content_hash: 86e0d415b2d2b9cd90151ce7d7e40510c258d558
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# linode-cli tickets

Manage Linode Support Tickets.
See also: `linode-cli`.
More information: <https://www.linode.com/docs/products/tools/cli/guides/account/>.

- List your Support Tickets:

`linode-cli tickets list`

- Open a new Ticket:

`linode-cli tickets create --summary "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Summary or quick title for the Ticket</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Detailed description of the issue</span>`"`

- List replies to a Ticket:

`linode-cli tickets replies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ticket_id</span>

- Reply to a specific Ticket:

`linode-cli tickets reply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ticket_id</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">The content of your reply</span>`"`
