---
layout: page
title: common/rscript (English)
description: "Run a script with the R programming language."
content_hash: ae03b71c17a0e3a61ebf3430923bf352ac066f3e
---
# Rscript

Run a script with the R programming language.
More information: <https://www.r-project.org>.

- Run a script:

`Rscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.R</span>

- Run a script in vanilla mode (i.e. a blank session that doesn't save the workspace at the end):

`Rscript --vanilla `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.R</span>

- Execute one or more R expressions:

`Rscript -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression1</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression2</span>

- Display R version:

`Rscript --version`
