---
layout: page
title: common/puppet-agent (English)
description: "Retrieves the client configuration from a Puppet server and applies it to the local host."
content_hash: 1f923897dce7a0bb8ba2b0ed394325708e569056
related_topics:
  - title: Deutsch version
    url: /de/common/puppet-agent.html
    icon: bi bi-globe
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
