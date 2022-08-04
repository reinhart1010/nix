---
layout: page
title: common/odps-resource (English)
description: "Manage resources in ODPS (Open Data Processing Service)."
content_hash: e656a62b8dbabd5ba47b637ace4b059fc295fcb9
---
# odps resource

Manage resources in ODPS (Open Data Processing Service).
See also `odps`.
More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Show resources in the current project:

`list resources;`

- Add file resource:

`add file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>`;`

- Add archive resource:

`add archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.tar.gz</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>`;`

- Add .jar resource:

`add jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package.jar</span>`;`

- Add .py resource:

`add py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>`;`

- Delete resource:

`drop resource `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>`;`
