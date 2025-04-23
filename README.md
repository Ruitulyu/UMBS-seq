# UMBS-seq
This Python script filters out non-bisulfite converted reads
=======
# Paired-End FASTQ Filter Script

This Python script filters **paired-end FASTQ files** by removing read pairs that exceed user-defined thresholds for nucleotide content:

- Removes **read pairs** where **Read 1 contains more than N 'C' bases**.
- And **Read 2 contains more than M 'G' bases**.

Supports both uncompressed `.fastq` and compressed `.fastq.gz` files.

---

## 🔧 Requirements

- Python 3.x

No external packages are required (uses only the Python standard library).

---

## 📥 Installation

Clone this repository:

```bash
git clone https://github.com/Ruitulyu/UMBS-seq.git
cd UMBS-seq
```

---

## 🚀 Usage

```bash
python filter_paired_fastq.py \
  --r1 input_R1.fastq.gz \
  --r2 input_R2.fastq.gz \
  --out_r1 filtered_R1.fastq.gz \
  --out_r2 filtered_R2.fastq.gz \
  --max_C 4 \
  --max_G 4
```
Only read pairs passing both filters will be retained in the output files.

## 📋 Arguments
|Argument   |Description	                             |Required	|Default    |
|   :---:   |                      :---:                     |   :---:  |   :---:   |
|--r1	    | Input Read 1 FASTQ file (.fastq or .fastq.gz)  |	✅	|N/A        |
|--r2	    | Input Read 2 FASTQ file (.fastq or .fastq.gz)  |	✅	|N/A        |
|--out_r1   | Output file for filtered Read 1                |	✅	|N/A        |
|--out_r2   | Output file for filtered Read 2	             |  ✅	|N/A        |
|--max_C    | Maximum number of 'C' bases allowed in Read 1  |	❌	|4          |
|--max_G    | Maximum number of 'G' bases allowed in Read 2  |	❌	|4          |
|--help     | Print the help                                 |  ❌      |N/A        |

## 🙌 Acknowledgments
Developed by Ruitu Lyu to support custom quality control of bisulfite and high-throughput sequencing data.
Feel free to submit issues or pull requests for feature requests or improvements.
