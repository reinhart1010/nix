---
layout: page
title: common/crane-version (English)
description: "Print the version of a binary."
content_hash: 7cd9a4615c963dfeff1a85a605bf70d190eb6b69
last_modified_at: 2024-10-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-version.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane version

Print the version of a binary.
The version string is completely dependent on how the binary was built, so you should not depend on the version format. It may change without notice.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_version.md>.

- Display version:

`crane version`

- Display help:

`crane version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
