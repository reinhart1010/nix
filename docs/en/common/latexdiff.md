---
layout: page
title: common/latexdiff (English)
description: "Determine differences between two LaTeX files."
content_hash: 66da7e9202cbd421065cf319da3b211f1bb01724
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# latexdiff

Determine differences between two LaTeX files.
More information: <https://ctan.org/pkg/latexdiff>.

- Determine changes between different versions of a LaTeX file (the resulting LaTeX file can be compiled to show differences underlined):

`latexdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.tex</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.tex</span>

- Determine changes between different versions of a LaTeX file by highlighting differences in boldface:

`latexdiff --type=BOLD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.tex</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.tex</span>

- Determine changes between different versions of a LaTeX file, and display minor changes in equations with both added and deleted graphics:

`latexdiff --math-markup=fine --graphics-markup=both `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.tex</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.tex</span>
