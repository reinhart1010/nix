---
layout: page
title: common/magento (English)
description: "Manage the Magento PHP framework."
content_hash: 7161775611b790fe82b7c9208ff531b30c9df592
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# magento

Manage the Magento PHP framework.
More information: <https://magento.com>.

- Enable one or more modules:

`magento module:enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module1 module2 ...</span>

- Disable one or more modules:

`magento module:disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module1 module2 ...</span>

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
