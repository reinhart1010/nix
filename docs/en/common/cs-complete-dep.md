---
layout: page
title: common/cs-complete-dep (English)
description: "Search for libraries without doing it directly on the web."
content_hash: bff3bcc4394e0d243646ae65c285b0674d5771cb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cs complete dep

Search for libraries without doing it directly on the web.
More information: <https://get-coursier.io/docs/cli-complete>.

- Print which artifacts are published under a specific Maven group identifier:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>

- List published library versions under a specific Maven group identifier and an artifact one:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>

- Print which artifacts are pubblished under a given Maven groupId searching in the ivy2local:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>` --repository ivy2local`

- List published artifacts under a Maven group identifier searching in a specific repository and credentials:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` --credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
