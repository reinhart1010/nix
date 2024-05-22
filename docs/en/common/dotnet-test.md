---
layout: page
title: common/dotnet-test (English)
description: "Execute tests for a .NET application."
content_hash: 2e8bf6c135df41d0f202b25ed3f38cfe060cc202
last_modified_at: 2024-05-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-test.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet test

Execute tests for a .NET application.
Note: View <https://learn.microsoft.com/en-us/dotnet/core/testing/selective-unit-tests> for supported filter expressions.
More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-test>.

- Execute tests for a .NET project/solution in the current directory:

`dotnet test`

- Execute tests for a .NET project/solution in a specific location:

`dotnet test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_or_solution</span>

- Execute tests matching the given filter expression:

`dotnet test --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name~TestMethod1</span>
