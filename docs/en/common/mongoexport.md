---
layout: page
title: common/mongoexport (English)
description: "Produce exports of data stored in a MongoDB instance formatted as JSON or CSV."
content_hash: 46ad56067a50acf303f4c301bc2739abbd61949e
---
# mongoexport

Produce exports of data stored in a MongoDB instance formatted as JSON or CSV.
More information: <https://docs.mongodb.com/database-tools/mongoexport/>.

- Export a collection to stdout, formatted as JSON:

`mongoexport --uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connection_string</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>

- Export the documents in the specified collection that match a query to a JSON file:

`mongoexport --db=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>` --query="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query_object</span>`" --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Export documents as a JSON array instead of one object per line:

`mongoexport --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>` --jsonArray`

- Export documents to a CSV file:

`mongoexport --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>` --fields="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field1,field2,...</span>`" --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Export documents that match the query in the specified file to a CSV file, omitting the list of field names on the first line:

`mongoexport --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>` --fields="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field1,field2,...</span>`" --queryFile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --noHeaderLine --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Export documents to stdout, formatted as human-readable JSON:

`mongoexport --uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mongodb_uri</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>` --pretty`

- Display help:

`mongoexport --help`
