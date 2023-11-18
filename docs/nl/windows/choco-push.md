---
layout: page
title: windows/choco-push (Nederlands)
description: "Push een gecompileerd NuGet pakket (`nupkg`) naar een pakketfeed."
content_hash: edc27f452da8e623ba129ef4104b09f613d3ad60
last_modified_at: 2023-11-18
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco-push

Push een gecompileerd NuGet pakket (`nupkg`) naar een pakketfeed.
Meer informatie: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Push een gecompileerd `nupkg` naar de gespecificeerde feed:

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>

- Push een gecompileerd `nupkg` naar de gespecificeerde feed met een timeout in seconden (standaard is 2700):

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>` --execution-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
