---
layout: page
title: common/fgrep (English)
description: "Matches fixed strings in files."
content_hash: 0a5d0d0a5a5cbe5e392126d2290c39b4fac3bf2b
last_modified_at: 2024-01-31
related_topics:
  - title: Nederlands version
    url: /nl/common/fgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fgrep

Matches fixed strings in files.
Equivalent to `grep -F`.
More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Search for an exact string in a file:

`fgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search only lines that match entirely in one or more files:

`fgrep -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Count the number of lines that match the given string in a file:

`fgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show the line number in the file along with the line matched:

`fgrep -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display all lines except those that contain the search string:

`fgrep -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display filenames whose content matches the search string at least once:

`fgrep -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
