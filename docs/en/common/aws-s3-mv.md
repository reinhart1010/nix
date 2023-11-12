---
layout: page
title: common/aws-s3-mv (English)
description: "Move local files or S3 objects to another location locally or in S3."
content_hash: 1161b422431e585fb091553a193d285b87fbe33b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# aws s3 mv

Move local files or S3 objects to another location locally or in S3.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html>.

- Move a file from local to a specified bucket:

`aws s3 mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_file</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_file</span>

- Move a specific S3 object into another bucket:

`aws s3 mv s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name2</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Move a specific S3 object into another bucket keeping the original name:

`aws s3 mv s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name2</span>

- Display help:

`aws s3 mv help`
