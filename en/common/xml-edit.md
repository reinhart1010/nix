---
layout: page
title: common/xml-edit (English)
description: "Edit an XML document."
content_hash: 1683049a96a4ebbcad38ac5957abb0b524ceb79e
---
# xml edit

Edit an XML document.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Delete elements matching an XPATH from an XML document:

`xml edit --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Move an element node of an XML document from XPATH1 to XPATH2:

`xml edit --move "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH2</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Rename all attributes named "id" to "ID":

`xml edit --rename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//*/@id</span>`" -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Rename sub-elements of the element "table" that are named "rec" to "record":

`xml edit --rename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/xml/table/rec</span>`" -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">record</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Update the XML table record with "id=3" to the value "id=5":

`xml edit --update "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml/table/rec[@id=3]/@id</span>`" -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Display help for the `edit` subcommand:

`xml edit --help`
