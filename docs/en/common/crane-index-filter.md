---
layout: page
title: common/crane-index-filter (English)
description: "Modifies a remote index by filtering based on platform."
content_hash: b5ac1b6accb52d12d122a334156a547dd5eb971a
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane index filter

Modifies a remote index by filtering based on platform.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- Modify remote index:

`crane index filter`

- Specify the platform(s) to keep from base in the form os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,<platform></span>`:

`crane index filter --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform1 platform2 ...</span>

- Tag to apply to resulting image:

`crane index filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tags</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Display help:

`crane index filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
