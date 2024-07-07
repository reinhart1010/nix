---
layout: page
title: common/huggingface-cli (English)
description: "Interact with Hugging Face Hub."
content_hash: 8634b27756ce7970fc97129f238b89e3e7133e3e
last_modified_at: 2024-07-07
tldri18n_status: 2
---
# huggingface-cli

Interact with Hugging Face Hub.
Login, manage local cache, download or upload files.
More information: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

- Login to Hugging Face Hub:

`huggingface-cli login`

- Display the name of the logged in user:

`huggingface-cli whoami`

- Log out:

`huggingface-cli logout`

- Print information about the environment:

`huggingface-cli env`

- Download files from an repository and print out the path (omit filenames to download entire repository):

`huggingface-cli download --repo-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename1 filename2 ...</span>

- Upload an entire folder or a file to Hugging Face:

`huggingface-cli upload --repo-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_file_or_directory</span>

- Scan cache to see downloaded repositories and their disk usage:

`huggingface-cli scan-cache`

- Delete the cache interactively:

`huggingface-cli delete-cache`
