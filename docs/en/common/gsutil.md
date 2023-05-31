---
layout: page
title: common/gsutil (English)
description: "The gsutil CLI lets you access Google Cloud Storage from the command-line."
content_hash: 7fbd3582b96ab9237e02eed6bfebe891582795e6
last_modified_at: 2023-05-31
---
# gsutil

The gsutil CLI lets you access Google Cloud Storage from the command-line.
You can use gsutil to do a wide range of bucket and object management tasks.
More information: <https://cloud.google.com/storage/docs/gsutil>.

- List all buckets in a project you are logged into:

`gsutil ls`

- List the objects in a bucket:

`gsutil ls -r 'gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>`**'`

- Download an object from a bucket:

`gsutil cp gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/save_location</span>

- Upload an object to a bucket:

`gsutil cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_location</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_bucket_name</span>`/`

- Rename or move objects in a bucket:

`gsutil mv gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_object_name</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_object_name</span>

- Create a new bucket in the project you are logged into:

`gsutil mb gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>

- Delete a bucket and remove all the objects in it:

`gsutil rm -r gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>
