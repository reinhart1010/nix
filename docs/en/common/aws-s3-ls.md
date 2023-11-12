---
layout: page
title: common/aws-s3-ls (English)
description: "List AWS S3 buckets, folders (prefixes), and files (objects)."
content_hash: f886b5bc97b5bf672f20f98be6e6a0048bbc359b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# aws s3 ls

List AWS S3 buckets, folders (prefixes), and files (objects).
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

- List all buckets:

`aws s3 ls`

- List files and folders in the root of a bucket (`s3://` is optional):

`aws s3 ls s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- List files and folders directly inside a directory:

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`/`

- List all files in a bucket:

`aws s3 ls --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- List all files in a path with a given prefix:

`aws s3 ls --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Display help:

`aws s3 ls help`
