---
layout: page
title: linux/compseq (English)
description: "Calculate the composition of unique words in sequences."
content_hash: 495e82c3dcb81382f444d080aa09a3f7d955a228
last_modified_at: 2024-05-16
tldri18n_status: 2
---
# compseq

Calculate the composition of unique words in sequences.
More information: <https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- Count observed frequencies of words in a FASTA file, providing parameter values with interactive prompt:

`compseq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fasta</span>

- Count observed frequencies of amino acid pairs from a FASTA file, save output to a text file:

`compseq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_protein.fasta</span>` -word 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.comp</span>

- Count observed frequencies of hexanucleotides from a FASTA file, save output to a text file and ignore zero counts:

`compseq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_dna.fasta</span>` -word 6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.comp</span>` -nozero`

- Count observed frequencies of codons in a particular reading frame; ignoring any overlapping counts (i.e. move window across by word-length 3):

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_rna.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.comp</span>` -nozero -frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Count observed frequencies of codons frame-shifted by 3 positions; ignoring any overlapping counts (should report all codons except the first one):

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_rna.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.comp</span>` -nozero -frame 3`

- Count amino acid triplets in a FASTA file and compare to a previous run of `compseq` to calculate expected and normalised frequency values:

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/human_proteome.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file1.comp</span>` -nozero -infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file2.comp</span>

- Approximate the above command without a previously prepared file, by calculating expected frequencies using the single base/residue frequencies in the supplied input sequence(s):

`compseq -sequence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/human_proteome.fasta</span>` -word 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.comp</span>` -nozero -calcfreq`

- Display help (use `-help -verbose` for more information on associated and general qualifiers):

`compseq -help`
