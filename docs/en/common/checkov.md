---
layout: page
title: common/checkov (English)
description: "Checkov is a static code analysis tool for Infrastructure as Code (IaC)."
content_hash: 3d658081aba10831e002da71a2f1d95ecb2f20d8
last_modified_at: 2024-03-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/checkov.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># checkov

Checkov is a static code analysis tool for Infrastructure as Code (IaC).
It is also a software composition analysis (SCA) tool for images and open source packages.
More information: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

- Scan a directory containing IaC (Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile, etc):

`checkov --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Scan an IaC file, omitting code blocks in the output:

`checkov --compact --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List all checks for all IaC types:

`checkov --list`
