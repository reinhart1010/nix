---
layout: page
title: common/quarto (English)
description: "An open-source scientific and technical publishing system built on Pandoc."
content_hash: ca372f0d3ce939068389094bdde634c3f35099fa
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# quarto

An open-source scientific and technical publishing system built on Pandoc.
More information: <https://quarto.org/>.

- Create a new project:

`quarto create-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">book|default|website</span>

- Create a new blog website:

`quarto create-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">website</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blog</span>

- Render input file(s) to different formats:

`quarto render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qmd|rmd|ipynb}</span>`} --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|pdf|docx</span>

- Render and preview a document or a website:

`quarto preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory|path/to/file</span>

- Publish a document or project to Quarto Pub, Github Pages, RStudio Connect or Netlify:

`quarto publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quarto-pub|gh-pages|connect|netlify</span>
