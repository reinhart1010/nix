---
layout: page
title: windows/choco-push (English)
description: "Push a compiled NuGet package (`nupkg`) to a package feed."
content_hash: 6a56f063b8627736e58eb57e0bc0da88bba0d3da
last_modified_at: 2023-11-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco-push

Push a compiled NuGet package (`nupkg`) to a package feed.
More information: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Push a compiled `nupkg` to the specified feed:

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>

- Push a compiled `nupkg` to the specified feed with a timeout in seconds (default is 2700):

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>` --execution-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
