---
layout: page
title: common/zstd (中文)
description: "使用 Zstandard 压缩来压缩 / 解压文件。"
content_hash: 35f86e5e0e0e5dfe4a05afdf5be9475239c36988
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/zstd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/zstd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zstd

使用 Zstandard 压缩来压缩 / 解压文件。
更多信息：<https://github.com/facebook/zstd>.

- 将一个文件压缩到一个 `.zst` 后缀的压缩文件中：

`zstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- 解压缩一个文件：

`zstd --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zst</span>

- 将文件解压缩到标准输出（`stdout`）：

`zstd --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zst</span>

- 使用指定的压缩等级来压缩一个文件.0 = 最差，19 = 最好（默认等级是 3）：

`zstd -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- 使用更多内存（解压或压缩时）来得到更高的压缩比：

`zstd --ultra -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
