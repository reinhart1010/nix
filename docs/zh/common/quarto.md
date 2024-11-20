---
layout: page
title: common/quarto (中文)
description: "一个基于 Pandoc 的开源科学和技术出版系统。"
content_hash: 1910ba83ab0f9d1a0672a95dc6a39c5a21abab7f
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/quarto.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/quarto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# quarto

一个基于 Pandoc 的开源科学和技术出版系统。
更多信息：<https://quarto.org/>.

- 创建一个新项目：

`quarto create-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">book|default|website</span>

- 创建一个新的博客网站：

`quarto create-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">website</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blog</span>

- 将输入文件渲染为不同格式：

`quarto render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qmd|rmd|ipynb}</span>`} --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|pdf|docx</span>

- 渲染并预览文档或网站：

`quarto preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录 | 路径/到/文件</span>

- 发布文档或项目到 Quarto Pub、Github Pages、RStudio Connect 或 Netlify：

`quarto publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quarto-pub|gh-pages|connect|netlify</span>
