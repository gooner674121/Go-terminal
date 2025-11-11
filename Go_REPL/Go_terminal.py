import os
import subprocess
import tempfile

print("Welcome to Go Terminal (created by Chase Stirling)!")
print("Type 'exit' to quit.")
print("Type 'run' to compile and execute your code.")
print("©2025 Robert Griesemer, Rob Pike, Ken Thompson, Chase Stirling")
print("---------------------------------------------")

code_lines = []

while True:
    line = input("Go> ")
    if line.strip().lower() == "exit":
        break
    elif line.strip().lower() == "run":
        if not code_lines:
            print("⚠️ No code to run!")
            continue
        # Remove accidental prompt if copied
        cleaned_code = [l.replace("Go> ", "") for l in code_lines]

        with tempfile.NamedTemporaryFile(delete=False, suffix=".go") as tmp_go:
            tmp_go.write("\n".join(cleaned_code).encode("utf-8"))
            tmp_go_path = tmp_go.name

        try:
            # Run Go program and capture both stdout and stderr
            proc = subprocess.Popen(["go", "run", tmp_go_path],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            out, err = proc.communicate()

            if out:
                print(out)  # print standard output
            if err:
                print("❌ Compilation/runtime errors:\n", err)
        except FileNotFoundError:
            print("⚠️ Go not found! Make sure Go is installed and in PATH.")
        finally:
            os.remove(tmp_go_path)
        code_lines = []
    else:
        code_lines.append(line)
