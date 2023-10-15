---
layout: page
title: common/aws-s3-rb (English)
description: "Delete an empty S3 bucket."
content_hash: 1147d086ff9cca37f9e847d4b6de0c2fd116dfb2
last_modified_at: 2023-10-15
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws s3 rb

Delete an empty S3 bucket.
More information: <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- Delete an empty S3 bucket:

`aws s3 rb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Force delete an S3 bucket and its non-versioned objects (will crash if versioned objects are present):

`aws s3 rb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --force`
