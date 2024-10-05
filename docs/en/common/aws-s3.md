---
layout: page
title: common/aws-s3 (English)
description: "CLI for AWS S3 - provides storage through web services interfaces."
content_hash: 0028d8f5e84f3616a2408ee2187cfddb8f9c98b9
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/aws-s3.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-s3.html
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
tldri18n_status: 2
---
# aws s3

CLI for AWS S3 - provides storage through web services interfaces.
Some subcommands such as `cp` have their own usage documentation.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Show files in a bucket:

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Sync files and directories from local to bucket:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Sync files and directories from bucket to local:

`aws s3 sync s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Sync files and directories with exclusions:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`/*`

- Remove file from bucket:

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Preview changes only:

`aws s3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any_command</span>` --dryrun`
