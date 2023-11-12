---
layout: page
title: osx/xcodes-runtimes (English)
description: "Manage Xcode Simulator runtimes."
content_hash: dc07dbf1d4c2b0ea2e78ae7a81c8b2064bdad44d
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes-runtimes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodes runtimes

Manage Xcode Simulator runtimes.
More information: <https://github.com/xcodesorg/xcodes>.

- Display all available Simulator runtimes:

`xcodes runtimes --include-betas`

- Download a Simulator runtime:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_name</span>

- Download and install a Simulator runtime:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_name</span>

- Download/install a Simulator runtime for specific iOS/watchOS/tvOS/visionOS version (must be written as case-sensitive):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iOS|watchOS|tvOS|visionOS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_version</span>`"`

- Set a specific location where the runtime archive will be first downloaded (defaults to `~/Downloads`):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_name</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Do not delete the downloaded archive when the Simulator is successfully installed:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime_name</span>` --keep-archive`
