---
layout: page
title: common/aws-s3-presign (English)
description: "Generate pre-signed URLs for Amazon S3 objects."
content_hash: a2f84ab2d6f2b833d20853828cb0b1df43770cb4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws s3 presign

Generate pre-signed URLs for Amazon S3 objects.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- Generate a pre-signed URL for a specific S3 object that is valid for one hour:

`aws s3 presign s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a pre-signed URL valid for a specific lifetime:

`aws s3 presign s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --expires-in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration_in_seconds</span>

- Display help:

`aws s3 presign help`
