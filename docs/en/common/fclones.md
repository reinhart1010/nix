---
layout: page
title: common/fclones (English)
description: "Efficient duplicate file finder and remover."
content_hash: 2e4e829a246ce2381075902522110e4e1889abd1
last_modified_at: 2024-03-26
tldri18n_status: 2
---
# fclones

Efficient duplicate file finder and remover.
More information: <https://github.com/pkolaczk/fclones>.

- Search for duplicate files in the current directory:

`fclones group .`

- Search multiple directories for duplicate files and cache the results:

`fclones group --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2</span>

- Search only the specified directory for duplicate files, skipping subdirectories and save the results into a file:

`fclones group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --depth 1 > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Move the duplicate files in a TXT file to a different directory:

`fclones move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Perform a dry run for soft links in a TXT file without actually linking:

`fclones link --soft < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` --dry-run 2 > /dev/null`

- Delete the newest duplicates from the current directory without storing them in a file:

`fclones group . | fclones remove --priority newest`

- Preprocess JPEG files in the current directory by using an external command to strip their EXIF data before matching for duplicates:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`
