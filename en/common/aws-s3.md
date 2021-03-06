---
layout: page
title: common/aws-s3 (English)
description: "CLI for AWS S3 - provides storage through web services interfaces."
content_hash: a0c0ea9ac755cecdeb4dcccd6ef1690ccf341b09
related_topics:
  - title: Deutsch version
    url: /de/common/aws-s3.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws-s3.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-s3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-s3.html
    icon: bi bi-globe
---
# aws s3

CLI for AWS S3 - provides storage through web services interfaces.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Show files in a bucket:

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Sync files and directories from local to bucket:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Sync files and directories from bucket to local:

`aws s3 sync s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Sync files and directories with exclusions:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`/*`

- Remove file from bucket:

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Preview changes only:

`aws s3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any_command</span>` --dryrun`
