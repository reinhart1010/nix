---
layout: page
title: common/gh-gist (中文)
description: "在命令行上使用 GitHub Gists."
content_hash: 40e256de973f2a344a40768f400b6fd97a82e0f3
related_topics:
  - title: English version
    url: /en/common/gh-gist.html
    icon: bi bi-globe
---
# gh gist

在命令行上使用 GitHub Gists.
更多信息：<https://cli.github.com/manual/gh_gist>.

- 从一个以空格分隔的文件列表中创建一个新的 Gist：

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件</span>

- 创建一个带有描述的新 Gist：

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` --desc "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">描述</span>`"`

- 编辑一个 Gist：

`gh gist edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_或_url</span>

- 列出当前登录用户所拥有的 Gist：

`gh gist list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">int</span>

- 在默认浏览器中查看 Gist，且不渲染 Markdown：

`gh gist view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_或_url</span>` --web --raw`
