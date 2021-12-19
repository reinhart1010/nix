---
layout: page
title: common/odps-inst (English)
description: "Manage instances in ODPS (Open Data Processing Service)."
content_hash: eb01e19a0c0eae2c73ad262e278d8e499178af92
---
# odps inst

Manage instances in ODPS (Open Data Processing Service).
See also `odps`.
More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Show instances created by current user:

`show instances;`

- Describe the details of an instance:

`desc instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_id</span>`;`

- Check the status of an instance:

`status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_id</span>`;`

- Wait on the termination of an instance, printing log and progress information until then:

`wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_id</span>`;`

- Kill an instance:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_id</span>`;`
