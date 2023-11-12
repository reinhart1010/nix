---
layout: page
title: common/llvd (English)
description: "Linkedin Learning Video Downloader."
content_hash: 834f45542d795ce88b69db4da9793bd23d01cd91
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# llvd

Linkedin Learning Video Downloader.
More information: <https://github.com/knowbee/llvd>.

- Download a [c]ourse using cookie-based authentication:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">course-slug</span>` --cookies`

- Download a course at a specific [r]esolution:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">course-slug</span>` -r 720`

- Download a course with [ca]ptions (subtitles):

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">course-slug</span>` --caption`

- Download a course [p]ath with [t]hrottling between 10 to 30 seconds:

`llvd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path-slug</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10,30</span>` --cookies`
