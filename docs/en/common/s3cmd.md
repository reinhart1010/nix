---
layout: page
title: common/s3cmd (English)
description: "Command line tool and client for uploading, retrieving and managing data in S3 compatible object storage."
content_hash: 03589cb7315a2f32420849ee9271c5b02dfb6deb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# s3cmd

Command line tool and client for uploading, retrieving and managing data in S3 compatible object storage.
More information: <https://s3tools.org/s3cmd>.

- Invoke configuration/reconfiguration tool:

`s3cmd --configure`

- List Buckets/Folders/Objects:

`s3cmd ls s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket|path/to/file</span>

- Create Bucket/Folder:

`s3cmd mb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>

- Download a specific file from a bucket:

`s3cmd get s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_file</span>

- Upload a file to a bucket:

`s3cmd put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_file</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Move an object to a specific bucket location:

`s3cmd mv s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src_bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src_object</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dst_bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dst_object</span>

- Delete a specific object:

`s3cmd rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object</span>
