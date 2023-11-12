---
layout: page
title: common/cradle-elastic (English)
description: "Manage the Elasticsearch instances for a Cradle instance."
content_hash: ec25cc7973da7a40048a2fc7d4c12f08c01c0de7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-elastic.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-elastic.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-elastic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle elastic

Manage the Elasticsearch instances for a Cradle instance.
More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Truncate the Elasticsearch index:

`cradle elastic flush`

- Truncate the Elasticsearch index for a specific package:

`cradle elastic flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Submit the Elasticsearch schema:

`cradle elastic map`

- Submit the Elasticsearch schema for a specific package:

`cradle elastic map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Populate the Elasticsearch indices for all packages:

`cradle elastic populate`

- Populate the Elasticsearch indices for a specific package:

`cradle elastic populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
