# simple command line entry
# src/cli.py
import argparse
from orchestrator import DatasetPipeline

def main():
    parser = argparse.ArgumentParser(description="Run Automated EDA Narrator")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--out", help="Output markdown path", default=None)
    args = parser.parse_args()
    pipeline = DatasetPipeline(args.csv)
    md = pipeline.run()
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote report to {args.out}")
    else:
        print(md)

if __name__ == "__main__":
    main()
