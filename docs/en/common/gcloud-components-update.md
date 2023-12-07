---
layout: page
title: common/gcloud-components-update (English)
description: "Update all your installed Google Cloud CLI components to the latest version."
content_hash: 344b30e52def9137d2d6476d61ffcc26aaf5f45d
last_modified_at: 2023-12-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-components-update.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud components update

Update all your installed Google Cloud CLI components to the latest version.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/components/update>.

- Update all components to the latest version:

`gcloud components update`

- Update all components to a specific version:

`gcloud components update --version=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>

- Update components without confirmation (useful for automation scripts):

`gcloud components update --quiet`
