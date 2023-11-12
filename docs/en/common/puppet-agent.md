---
layout: page
title: common/puppet-agent (English)
description: "Retrieves the client configuration from a Puppet server and applies it to the local host."
content_hash: 16d1fb26f3a75feecd3a0f36cfdc908f2885abee
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/puppet-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# puppet agent

Retrieves the client configuration from a Puppet server and applies it to the local host.
More information: <https://puppet.com/docs/puppet/7/man/agent.html>.

- Register a node at a Puppet server and apply the received catalog:

`puppet agent --test --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puppetserver_fqdn</span>` --serverport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --waitforcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poll_time</span>

- Run the agent in the background (uses settings from `puppet.conf`):

`puppet agent`

- Run the agent once in the foreground, then exit:

`puppet agent --test`

- Run the agent in dry-mode:

`puppet agent --test --noop`

- Log every resource being evaluated (even if nothing is being changed):

`puppet agent --test --evaltrace`

- Disable the agent:

`puppet agent --disable "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Enable the agent:

`puppet agent --enable`
