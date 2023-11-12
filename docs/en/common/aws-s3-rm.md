---
layout: page
title: common/aws-s3-rm (English)
description: "Delete S3 objects."
content_hash: 9d31738667ca1a3b3ef2a5e6d193fe411b35f5b2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# aws s3 rm

Delete S3 objects.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>.

- Delete a specific S3 object:

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Preview the deletion of a specific S3 object without deleting it (dry-run):

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --dryrun`

- Delete an object from a specific S3 access point:

`aws s3 rm s3://arn:aws:s3:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_point</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_point_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_key</span>

- Display help:

`aws s3 rm help`
