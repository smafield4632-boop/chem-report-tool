import subprocess, pathlib

NB = "notebooks/03_conductivity.ipynb"

subprocess.run([
    "jupyter", "nbconvert", "--to", "markdown", "--execute", NB,
    "--no-input",
    "--output-dir", "output", "--output", "report",
], check=True)

cmd = ["pandoc", "report.md", "-o", "report.docx",
       "-f", "markdown-implicit_figures"]
if pathlib.Path("templates/reference.docx").exists():
    cmd += ["--reference-doc", "../templates/reference.docx"]
subprocess.run(cmd, cwd="output", check=True)

print("→ output/report.docx")