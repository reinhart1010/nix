---
layout: page
title: common/sqsc (English)
description: "A command-line AWS Simple Queue Service client."
content_hash: 2d72ff4a7a8570a60793e10712a7a4b3285d1e30
---
# sqsc

A command-line AWS Simple Queue Service client.
More information: <https://github.com/yongfei25/sqsc>.

- List all queues:

`sqsc lq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_prefix</span>

- List all messages in a queue:

`sqsc ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- Copy all messages from one queue to another:

`sqsc cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_queue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_queue</span>

- Move all messages from one queue to another:

`sqsc mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_queue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_queue</span>

- Describe a queue:

`sqsc describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>

- Query a queue with SQL syntax:

`sqsc query "SELECT body FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` WHERE body LIKE '%user%'"`

- Pull all messages from a queue into a local SQLite database in your present working directory:

`sqsc pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>
