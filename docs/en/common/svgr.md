---
layout: page
title: common/svgr (English)
description: "Transform SVGs into React components."
content_hash: ce791ac04252a817b4c4b28554b5b3965986979e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# svgr

Transform SVGs into React components.
More information: <https://react-svgr.com>.

- Transform a SVG file into a React component to `stdout`:

`svgr -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Transform a SVG file into a React component using TypeScript to `stdout`:

`svgr --typescript -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Transform a SVG file into a React component using JSX transform to `stdout`:

`svgr --jsx-runtime automatic -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>

- Transform all SVG files from a directory to React components into a specific directory:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>

- Transform all SVG files from a directory to React components into a specific directory skipping already transformed files:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --ignore-existing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>

- Transform all SVG files from a directory to React components into a specific directory using a specific case for filenames:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --filename-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camel|kebab|pascal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>

- Transform all SVG files from a directory to React components into a specific directory without generating an index file:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>
