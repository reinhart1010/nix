---
layout: page
title: common/colima (English)
description: "Container runtimes for macOS and Linux with minimal setup."
content_hash: 70ec7357ddb788dcb7d4f0b583c4f5fe8d0fd20b
last_modified_at: 2024-03-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/colima.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># colima

Container runtimes for macOS and Linux with minimal setup.
More information: <https://github.com/abiosoft/colima>.

- Start the daemon in the background:

`colima start`

- Create a configuration file and use it:

`colima start --edit`

- Start and setup containerd (install `nerdctl` to use containerd via `nerdctl`):

`colima start --runtime containerd`

- Start with Kubernetes (`kubectl` is required):

`colima start --kubernetes`

- Customize CPU count, RAM memory and disk space (in GiB):

`colima start --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory</span>` --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_space</span>

- Use Docker via Colima (Docker is required):

`colima start`

- List containers with their information and status:

`colima list`

- Show runtime status:

`colima status`
