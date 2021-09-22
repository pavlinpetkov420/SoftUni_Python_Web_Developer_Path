import os
from pathlib import Path


def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        file_name, extension = file.split('.')
        if file_name not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


def extract_files(directories):
    return [el for el in directories if "." in el]


dir_content = os.listdir()

files = extract_files(dir_content)
report = get_report_for_files_extensions(files)
result_str = ""
for extension, file_names in sorted(report.items(), key=lambda x: x[0]):
    result_str += f".{extension}\n"
    for name in file_names:
        result_str += f"- - -{name}.{extension}\n"


desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop") + os.path.sep + "report.txt"

with open(desktop_path, 'w') as file:
    file.write(result_str)

