---
layout: page
title: common/go-clean (English)
description: "Remove object files and cached files."
content_hash: 708a9585361b6055dd24720e773909448b4017be
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-clean.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go clean

Remove object files and cached files.
More information: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- Print the remove commands instead of actually removing anything:

`go clean -n`

- Delete the build cache:

`go clean -cache`

- Delete all cached test results:

`go clean -testcache`

- Delete the module cache:

`go clean -modcache`
