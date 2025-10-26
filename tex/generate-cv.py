import yaml
from jinja2 import Environment, FileSystemLoader
import subprocess
import os

# Load YAML data
with open("data.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Load and render Jinja2–LaTeX template
env = Environment(loader=FileSystemLoader("./"))
template = env.get_template("cv-template.tex")
rendered_tex = template.render(data)

# Write rendered TeX file
with open("output.tex", "w", encoding="utf-8") as f:
    f.write(rendered_tex)

# Compile to PDF using pdflatex
subprocess.run(["pdflatex", "-interaction=nonstopmode", "output.tex"])

# Clean up auxiliary files
for ext in ["aux", "log"]:
    if os.path.exists(f"output.{ext}"):
        os.remove(f"output.{ext}")

print("✅ CV generated: output.pdf")
