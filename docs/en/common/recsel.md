---
layout: page
title: common/recsel (English)
description: "Print records from a recfile: a human-editable, plain text database."
content_hash: e7a18193b007572db5851eebb59b57fc302c0209
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# recsel

Print records from a recfile: a human-editable, plain text database.
More information: <https://www.gnu.org/software/recutils/manual/recutils.html>.

- Extract name and version field:

`recsel -p name,version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.rec</span>

- Use "~" to match a string with a given regular expression:

`recsel -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>` ~ '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.rec</span>`"`

- Use a predicate to match a name and a version:

`recsel -e "name ~ '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`' && version ~ '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.rec</span>
