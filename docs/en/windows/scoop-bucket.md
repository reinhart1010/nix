---
layout: page
title: windows/scoop-bucket (English)
description: "Manage buckets: Git repositories containing files which describe how scoop installs applications."
content_hash: 51bd5a5300e9733a378019ae7d00b5b6c55a19c2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop-bucket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop bucket

Manage buckets: Git repositories containing files which describe how scoop installs applications.
If Scoop doesn't know where the bucket is located its repository location must be specified.
More information: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- List all buckets currently in use:

`scoop bucket list`

- List all known buckets:

`scoop bucket known`

- Add a known bucket by its name:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Add an unknown bucket by its name and Git repository URL:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/repository.git</span>

- Remove a bucket by its name:

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
