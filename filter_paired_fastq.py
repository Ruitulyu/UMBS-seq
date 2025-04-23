import argparse
import gzip

def open_file(filename, mode='rt'):
    """Open a file normally or with gzip depending on its extension."""
    if filename.endswith('.gz'):
        return gzip.open(filename, mode)
    else:
        return open(filename, mode)

def filter_paired_fastq(r1_input, r2_input, r1_output, r2_output, max_C, max_G):
    with open_file(r1_input) as r1_in, open_file(r2_input) as r2_in, \
         open_file(r1_output, 'wt') as r1_out, open_file(r2_output, 'wt') as r2_out:
        while True:
            r1_header = r1_in.readline()
            r1_seq = r1_in.readline().strip()
            r1_plus = r1_in.readline()
            r1_qual = r1_in.readline()

            r2_header = r2_in.readline()
            r2_seq = r2_in.readline().strip()
            r2_plus = r2_in.readline()
            r2_qual = r2_in.readline()

            if not r1_qual or not r2_qual:
                break  # End of file

            if r1_seq.count('C') > max_C and r2_seq.count('G') > max_G:
                continue  # Skip this read pair

            r1_out.write(f"{r1_header}{r1_seq}\n{r1_plus}{r1_qual}")
            r2_out.write(f"{r2_header}{r2_seq}\n{r2_plus}{r2_qual}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Filter paired-end FASTQ reads where Read 1 has > max_C 'C's and Read 2 has > max_G 'G's."
    )
    parser.add_argument("--r1", required=True, help="Input Read 1 FASTQ file (.fastq or .fastq.gz)")
    parser.add_argument("--r2", required=True, help="Input Read 2 FASTQ file (.fastq or .fastq.gz)")
    parser.add_argument("--out_r1", required=True, help="Output filtered Read 1 FASTQ file")
    parser.add_argument("--out_r2", required=True, help="Output filtered Read 2 FASTQ file")
    parser.add_argument("--max_C", type=int, default=4, help="Maximum number of 'C's allowed in Read 1 [default: 4]")
    parser.add_argument("--max_G", type=int, default=4, help="Maximum number of 'G's allowed in Read 2 [default: 4]")

    args = parser.parse_args()
    filter_paired_fastq(args.r1, args.r2, args.out_r1, args.out_r2, args.max_C, args.max_G)
