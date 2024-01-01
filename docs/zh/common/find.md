---
layout: page
title: common/find (中文)
description: "在指定目录树下递归查找文件或目录。"
content_hash: e70c414e5804dc29a0437f185e0b0204e7506663
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/find.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

在指定目录树下递归查找文件或目录。
更多信息：<https://manned.org/find>.

- 通过扩展名查找文件：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- 查找匹配多个路径或名称模式的文件：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/path/**/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*pattern*</span>`'`

- 查找匹配指定名称的目录，不区分大小写：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*lib*</span>`'`

- 查找匹配指定模式的文件，排除特定路径：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/site-packages/*</span>`'`

- 查找符合指定大小范围的文件，将递归深度限制为 "1"：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- 对每个文件运行命令（在命令中使用 `{}` 代表当前文件）：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l {} </span>`\;`

- 查找最近 7 天修改的文件：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -daystart -mtime -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- 查找空（0 字节）的文件并删除：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f</span>` -empty -delete`
