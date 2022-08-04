---
layout: page
title: common/odps-func (English)
description: "Manage functions in ODPS (Open Data Processing Service)."
content_hash: 3bbc4aca84b060555282ec1aaa0bb2eaa8ac8b14
---
# odps func

Manage functions in ODPS (Open Data Processing Service).
See also `odps`.
More information: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Show functions in the current project:

`list functions;`

- Create a Java function using a `.jar` resource:

`create function `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">func_name</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path.to.package.Func</span>` using '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package.jar</span>`';`

- Create a Python function using a `.py` resource:

`create function `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">func_name</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.Func</span>` using '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>`';`

- Delete a function:

`drop function `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">func_name</span>`;`
