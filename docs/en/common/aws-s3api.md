---
layout: page
title: common/aws-s3api (English)
description: "Create and delete Amazon S3 buckets and edit bucket properties."
content_hash: 183c1894a15129db5c4ab4322182866e40bb89e0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# aws s3api

Create and delete Amazon S3 buckets and edit bucket properties.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html>.

- Create bucket in a specific region:

`aws s3api create-bucket --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --create-bucket-configuration LocationConstraint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- Delete a bucket:

`aws s3api delete-bucket --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- List buckets:

`aws s3api list-buckets`

- List the objects inside of a bucket and only show each object's key and size:

`aws s3api list-objects --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Contents[].{Key: Key, Size: Size}</span>`'`

- Add an object to a bucket:

`aws s3api put-object --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_key</span>` --body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Download object from a bucket (The output file is always the last argument):

`aws s3api get-object --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Apply an Amazon S3 bucket policy to a specified bucket:

`aws s3api put-bucket-policy --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --policy file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bucket_policy.json</span>

- Download the Amazon S3 bucket policy from a specified bucket:

`aws s3api get-bucket-policy --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --query Policy --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|table|text|yaml|yaml-stream</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bucket_policy</span>
