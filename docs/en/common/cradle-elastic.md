---
layout: page
title: common/cradle-elastic (English)
description: "Manage the Elasticsearch instances for a Cradle instance."
content_hash: 2dff576f0cc83f1aaac774602d1d968f4ae4b1c1
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
---
# cradle elastic

Manage the Elasticsearch instances for a Cradle instance.
More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Truncate the Elasticsearch index:

`cradle elastic flush`

- Truncate the Elasticsearch index for a specific package:

`cradle elastic flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Submit the Elasticsearch schema:

`cradle elastic map`

- Submit the Elasticsearch schema for a specific package:

`cradle elastic map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Populate the Elasticsearch indices for all packages:

`cradle elastic populate`

- Populate the Elasticsearch indices for a specific package:

`cradle elastic populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
