---
layout: page
title: common/kopia (English)
description: "Fast, secure open-source backup tool."
content_hash: bb9b4f41632c14afdd2b19ac8adccc1f35230d48
last_modified_at: 2024-01-16
tldri18n_status: 2
---
# kopia

Fast, secure open-source backup tool.
Supports encryption, compression, deduplication, and incremental snapshots.
More information: <https://kopia.io/docs/reference/command-line/>.

- Create a repository in the local filesystem:

`kopia repository create filesystem --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_repository</span>

- Create a repository on Amazon S3:

`kopia repository create s3 --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --access-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AWS_access_key_id</span>` --secret-access-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AWS_secret_access_key</span>

- Connect to a repository:

`kopia repository connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_type</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>

- Create a snapshot of a directory:

`kopia snapshot create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List snapshots:

`kopia snapshot list`

- Restore a snapshot to a specific directory:

`kopia snapshot restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Create a new policy:

`kopia policy set --global --keep-latest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_snapshots_to_keep</span>` --compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compression_algorithm</span>

- Ignore a specific file or folder from backups:

`kopia policy set --global --add-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_folder</span>
