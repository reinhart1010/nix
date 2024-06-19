---
layout: page
title: osx/shuf (中文)
description: "生成随机排列。"
content_hash: 947fe351bd330e59f946f965828628d43fc12bea
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

生成随机排列。
更多信息：<https://keith.github.io/xcode-man-pages/shuf.1.html>.

- 随机化文件中的行顺序并输出结果：

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 只输出结果的前 5 条：

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将结果输出写入另一个文件：

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件</span>

- 生成范围（1-10）内的随机数：

`shuf --input-range=1-10`
