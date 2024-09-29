---
layout: page
title: common/linode-cli-tickets (English)
description: "Manage Linode Support Tickets."
content_hash: 327721e7e2ccba16d0e22cb26b68cf61f190305a
last_modified_at: 2024-09-29
tldri18n_status: 2
---
# linode-cli tickets

Manage Linode Support Tickets.
See also: `linode-cli`.
More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>.

- List your Support Tickets:

`linode-cli tickets list`

- Open a new Ticket:

`linode-cli tickets create --summary "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Summary or quick title for the Ticket</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Detailed description of the issue</span>`"`

- List replies to a Ticket:

`linode-cli tickets replies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ticket_id</span>

- Reply to a specific Ticket:

`linode-cli tickets reply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ticket_id</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">The content of your reply</span>`"`
