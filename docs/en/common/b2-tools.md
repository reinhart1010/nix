---
layout: page
title: common/b2-tools (English)
description: "Access all features of Backblaze B2 Cloud Storage easily."
content_hash: d203af2795d33fe5a547a8a4e91a68b8a707da66
last_modified_at: 2024-08-07
tldri18n_status: 2
---
# b2-tools

Access all features of Backblaze B2 Cloud Storage easily.
More information: <https://www.backblaze.com/docs/cloud-storage-command-line-tools>.

- Access your account:

`b2 authorize_account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>

- List the existing buckets in your account:

`b2 list_buckets`

- Create a bucket, provide the bucket name, and access type (e.g. allPublic or allPrivate):

`b2 create_bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">allPublic|allPrivate</span>

- Upload a file. Choose a file, bucket, and a folder:

`b2 upload_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder_name</span>

- Upload a source directory to a Backblaze B2 bucket destination:

`b2 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Copy a file from one bucket to another bucket:

`b2 copy-file-by-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_bucket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/b2_file</span>

- Show the files in your bucket:

`b2 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Remove a "folder" or a set of files matching a pattern:

`b2 rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/folder|pattern</span>
