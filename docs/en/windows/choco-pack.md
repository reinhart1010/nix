---
layout: page
title: windows/choco-pack (English)
description: "Package a NuGet specification into a nupkg file."
content_hash: ae2f4fac0adb31c0461cabb48bd8cf645c8cd5ef
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pack.html
    icon: bi bi-globe
---
# choco pack

Package a NuGet specification into a nupkg file.
More information: <https://chocolatey.org/docs/commands-pack>.

- Package a NuGet specification to a nupkg file:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/specification</span>

- Package a NuGet specification specifying the version of the resulting file:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/specification</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Package a NuGet specification to a specific directory:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/specification</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>
