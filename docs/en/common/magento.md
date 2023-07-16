---
layout: page
title: common/magento (English)
description: "Manage the Magento PHP framework."
content_hash: 759629bf285784f1f3b322c68c3c27d2440bf0c4
last_modified_at: 2023-07-16
---
# magento

Manage the Magento PHP framework.
More information: <https://magento.com>.

- Enable one or more space-separated modules:

`magento module:enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module(s)</span>

- Disable one or more space-separated modules:

`magento module:disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module(s)</span>

- Update the database after enabling modules:

`magento setup:upgrade`

- Update code and dependency injection configuration:

`magento setup:di:compile`

- Deploy static assets:

`magento setup:static-content:deploy`

- Enable maintenance mode:

`magento maintenance:enable`

- Disable maintenance mode:

`magento maintenance:disable`

- List all available commands:

`magento list`
