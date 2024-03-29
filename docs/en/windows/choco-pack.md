---
layout: page
title: windows/choco-pack (English)
description: "Package a NuGet specification into a `nupkg` file."
content_hash: b6d7df84bbf7e4d4b282e278b06941054e0ef012
last_modified_at: 2023-11-17
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco pack

Package a NuGet specification into a `nupkg` file.
More information: <https://chocolatey.org/docs/commands-pack>.

- Package a NuGet specification to a `nupkg` file:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\specification_file</span>

- Package a NuGet specification specifying the version of the resulting file:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\specification_file</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Package a NuGet specification to a specific directory:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\specification_file</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\output_directory</span>
