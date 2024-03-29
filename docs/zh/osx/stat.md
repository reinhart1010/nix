---
layout: page
title: osx/stat (中文)
description: "显示文件状态。"
content_hash: d45f390e92587e42233c49758f802cb4ec04ab42
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

显示文件状态。
更多信息：<https://keith.github.io/xcode-man-pages/stat.1.html>.

- 显示文件属性，如大小、权限、创建和访问日期等：

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 与上面相同，但更详细（更类似于 Linux 的 `stat`）：

`stat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 只显示文件权限：

`stat -f %Mp%Lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 显示文件的所有者和所属组：

`stat -f "%Su %Sg" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 以字节为单位显示文件的大小：

`stat -f "%z %N" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>
