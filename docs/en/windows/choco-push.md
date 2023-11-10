---
layout: page
title: windows/choco-push (English)
description: "Push a compiled NuGet package (`nupkg`) to a package feed."
content_hash: 6a56f063b8627736e58eb57e0bc0da88bba0d3da
last_modified_at: 2023-11-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco-push

Push a compiled NuGet package (`nupkg`) to a package feed.
More information: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Push a compiled `nupkg` to the specified feed:

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>

- Push a compiled `nupkg` to the specified feed with a timeout in seconds (default is 2700):

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>` --execution-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
