---
layout: page
title: common/znew (中文)
description: "将文件从 `.Z` 格式重新压缩为 gzip 格式。"
content_hash: 6d692d7ebd060f5324acc6e8c8ed35d982b3fa8b
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/znew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/znew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# znew

将文件从 `.Z` 格式重新压缩为 gzip 格式。
更多信息：<https://manned.org/znew>.

- 将文件从 `.Z` 格式重新压缩为 gzip 格式：

`znew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.Z</span>

- 重新压缩多个文件，并显示每个文件所实现的压缩率%：

`znew -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.Z 路径/到/文件2.Z ...</span>

- 使用最慢的压缩方法重新压缩文件（以获得最佳压缩效果）：

`znew -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.Z</span>

- 重新压缩文件，如果 `.Z` 文件比 gzip 文件小，则保留 `.Z` 文件：

`znew -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.Z</span>
