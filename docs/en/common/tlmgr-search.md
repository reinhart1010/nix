---
layout: page
title: common/tlmgr-search (English)
description: "Search for TeX Live packages using (Perl) regular expressions."
content_hash: f58dda41367311c721a1b44f98b8bc2e4d545dcb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr search

Search for TeX Live packages using (Perl) regular expressions.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Search for a package name and descriptions of all locally installed packages from a specific regular expression:

`tlmgr search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`

- Search for all file names of all locally installed packages from a regular expression:

`tlmgr search --file "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`

- Search for all file names, package names, and descriptions of all locally installed packages from a regular expression:

`tlmgr search --all "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`

- Search the TeX Live database, instead of the local installation:

`tlmgr search --global "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`

- Restrict the matches for package names and descriptions (but not for file names) to whole words:

`tlmgr search --all --word "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`
