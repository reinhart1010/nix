---
layout: page
title: common/shards (English)
description: "Dependency management tool for the Crystal language."
content_hash: c81007b13d827118a060082f7d62862adf132014
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/common/shards.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shards

Dependency management tool for the Crystal language.
More information: <https://crystal-lang.org/reference/the_shards_command>.

- Create a skeleton `shard.yml` file:

`shards init`

- Install dependencies from a `shard.yml` file:

`shards install`

- Update all dependencies:

`shards update`

- List all installed dependencies:

`shards list`

- Display version of dependency:

`shards version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dependency_directory</span>
