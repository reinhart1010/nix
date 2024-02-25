---
layout: page
title: common/trufflehog (English)
description: "Find and verify credentials in files, Git repositories, S3 buckets, and Docker images."
content_hash: fd4f2b38b9623191760f9aae7bf0862c447d8d11
last_modified_at: 2024-02-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/trufflehog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trufflehog

Find and verify credentials in files, Git repositories, S3 buckets, and Docker images.
More information: <https://github.com/trufflesecurity/trufflehog>.

- Scan a Git repository for verified secrets:

`trufflehog git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --only-verified`

- Scan a GitHub organization for verified secrets:

`trufflehog github --org=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trufflesecurity</span>` --only-verified`

- Scan a GitHub repository for verified keys and get JSON output:

`trufflehog git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --only-verified --json`

- Scan a GitHub repository along with its Issues and Pull Requests:

`trufflehog github --repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --issue-comments --pr-comments`

- Scan an S3 bucket for verified keys:

`trufflehog s3 --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket name</span>` --only-verified`

- Scan S3 buckets using IAM Roles:

`trufflehog s3 --role-arn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iam-role-arn</span>

- Scan individual files or directories:

`trufflehog filesystem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Scan a Docker image for verified secrets:

`trufflehog docker --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trufflesecurity/secrets</span>` --only-verified`
