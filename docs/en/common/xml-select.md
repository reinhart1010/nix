---
layout: page
title: common/xml-select (English)
description: "Select from XML documents using XPATHs."
content_hash: b07616e712b2fc90d2e2478d16f1d1d8dff903cf
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml select

Select from XML documents using XPATHs.
Tip: use `xml elements` to display the XPATHs of an XML document.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Select all elements matching "XPATH1" and print the value of their sub-element "XPATH2":

`xml select --template --match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" --value-of "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH2</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Match "XPATH1" and print the value of "XPATH2" as text with new-lines:

`xml select --text --template --match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" --value-of "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH2</span>`" --nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Count the elements of "XPATH1":

`xml select --template --value-of "count(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`)" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Count all nodes in one or more XML documents:

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.xml|URI</span>

- Display help:

`xml select --help`
