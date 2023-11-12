---
layout: page
title: common/aws-s3-mb (English)
description: "Create S3 buckets."
content_hash: 694d3e9f686a507dda91e7571b144781a8312025
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# aws s3 mb

Create S3 buckets.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mb.html>.

- Create an S3 bucket:

`aws s3 mb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Create an S3 bucket in a specific region:

`aws s3 mb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- Display help:

`aws s3 mb help`
