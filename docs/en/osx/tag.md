---
layout: page
title: osx/tag (English)
description: "Edit tags on Mac OS X files (10.9 Mavericks and above)."
content_hash: 8d7676df1c2aea832593b5271f6695054ac2a861
last_modified_at: 2024-12-17
tldri18n_status: 2
---
# tag

Edit tags on Mac OS X files (10.9 Mavericks and above).
More information: <https://github.com/jdberry/tag/>.

- Add tags to a file:

`tag --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name1,tag_name2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove a tag:

`tag --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove all tags from a file:

`tag --remove \* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show all files with a given tag:

`tag --match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>
