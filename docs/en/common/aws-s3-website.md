---
layout: page
title: common/aws-s3-website (English)
description: "Set the website configuration for a bucket."
content_hash: bfa94748d64ccebc28de89f1dbbdebe198ae3e00
last_modified_at: 2023-12-04
tldri18n_status: 2
---
# aws s3 website

Set the website configuration for a bucket.
See also: `aws s3`.
More information: <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>.

- Configure a bucket as a static website:

`aws s3 website `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s3://bucket-name</span>` --index-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>

- Configure an error page for the website:

`aws s3 website `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s3://bucket-name</span>` --index-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` --error-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error.html</span>
