---
layout: page
title: common/stolonctl (English)
description: "CLI for Stolon, a cloud native PostgreSQL manager for PostgreSQL high availability."
content_hash: 6e73ff40e2439bdf17eaab4e03dead399fc7ea12
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# stolonctl

CLI for Stolon, a cloud native PostgreSQL manager for PostgreSQL high availability.
More information: <https://github.com/sorintlab/stolon>.

- Get cluster status:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_backend</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_endpoints</span>` status`

- Get cluster data:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_backend</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_endpoints</span>` clusterdata`

- Get cluster specification:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_backend</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_endpoints</span>` spec`

- Update cluster specification with a patch in JSON format:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_backend</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_endpoints</span>` update --patch '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_spec</span>`'`
