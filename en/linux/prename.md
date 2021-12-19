---
layout: page
title: linux/prename (English)
description: "Rename multiple files."
content_hash: 7998c07c0491fb89cfe6b9997717b4ea9a82f986
---
# rename

Rename multiple files.
NOTE: this page refers to the command from the `prename` Fedora package.

- Rename files using a Perl Common Regular Expression (substitute 'foo' with 'bar' wherever found):

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Dry-run - display which renames would occur without performing them:

`rename -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Force renaming even if the operation would remove existing destination files:

`rename -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'s/foo/bar/'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Convert filenames to lower case (use `-f` in case-insensitive filesystems to prevent "already exists" errors):

`rename 'y/A-Z/a-z/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Replace whitespace with underscores:

`rename 's/\s+/_/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>
