---
layout: page
title: osx/hdiutil (English)
description: "Utility to create and manage disk images."
content_hash: ece96025947a87ce2eeee7fd9d6bb7f989075581
---
# hdiutil

Utility to create and manage disk images.
More information: <https://ss64.com/osx/hdiutil.html>.

- Mount an image:

`hdiutil attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Unmount an image:

`hdiutil detach /Volumes/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>

- List mounted images:

`hdiutil info`

- Create an ISO image from the contents of a directory:

`hdiutil makehybrid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
