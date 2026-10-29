from pathlib import Path
from datetime import datetime
import sys

root = Path.cwd()
main_file = root / "backend" / "main.py"
panel_file = root / "src" / "components" / "JudgePanel.tsx"

if not main_file.exists() or not panel_file.exists():
    sys.exit("ERROR: Project files not found.")

main = main_file.read_text(encoding="utf-8-sig")
panel = panel_file.read_text(encoding="utf-8-sig")

# ---------------------------------------------
# 1. Update FastAPI public test data
# ---------------------------------------------

old_import = (
    "from test_cases import "
    "TEST_CASES, PUBLIC_TEST_COUNT, build_setup"
)

new_import = (
    "from test_cases import "
    "TEST_CASES, PUBLIC_TEST_COUNT, "
    "PUBLIC_CASE_DETAILS, build_setup"
)

if old_import in main:
    main = main.replace(old_import, new_import, 1)
elif "PUBLIC_CASE_DETAILS" not in main:
    sys.exit("ERROR: Unexpected main.py import structure.")

start_marker = '@app.get("/api/questions")'
end_marker = "# Paths"

start = main.find(start_marker)
end = main.find(end_marker, start)

if start < 0 or end < 0:
    sys.exit("ERROR: Cannot locate the question API.")

# Preserve the section separator before Paths.
section_start = main.rfind(
    "# ---------------------------------------------------------",
    start,
    end
)

if section_start < 0:
    sys.exit("ERROR: Cannot locate the Paths separator.")

new_api = '''@app.get("/api/questions")
def get_questions():
    result = []

    for question in QUESTIONS:
        question_id = question["id"]
        mode = practice_mode(question)

        case = (
            TEST_CASES.get(question_id, {})
            if mode == "coding"
            else {}
        )

        all_tests = case.get("tests", {})

        public_count = (
            public_test_count(question_id)
            if case
            else 0
        )

        details = PUBLIC_CASE_DETAILS.get(
            question_id, {}
        )

        visible_tests = []

        for name in list(all_tests)[:public_count]:
            spec = details.get(name, {})

            visible_tests.append({
                "name": name,
                "input": spec.get("input"),
                "expected": (
                    repr(spec["expected"])
                    if "expected" in spec
                    else None
                ),
            })

        result.append({
            **enrich_question(
                public_question(question)
            ),
            "practiceMode": mode,
            "testsAvailable": bool(case),
            "visibleTests": visible_tests,
            "publicTestCount": public_count,
            "hiddenTestCount": max(
                0,
                len(all_tests) - public_count
            ),
        })

    return result


# ---------------------------------------------------------
'''

main = main[:start] + new_api + main[section_start:]

# ---------------------------------------------
# 2. Update the React test-case panel
# ---------------------------------------------

old_type = "visibleTests?:string[];"
new_type = "visibleTests?:(string|PublicCase)[];"

if old_type not in panel:
    sys.exit("ERROR: Unexpected JudgePanel.tsx props.")

panel = panel.replace(
    old_type,
    new_type,
    1
)

panel = panel.replace(
    "type Props=",
    "type PublicCase={"
    "name:string;"
    "input?:string|null;"
    "expected?:string|null"
    "};\ntype Props=",
    1
)

old_input = (
    "{examples[selected]?.input??"
    "visibleTests[selected]??'Not available'}"
)

new_input = (
    "{typeof visibleTests[selected]==='object' "
    "&& visibleTests[selected]!==null "
    "? ((visibleTests[selected] as PublicCase).input "
    "?? 'Input not yet configured') "
    ": (examples[selected]?.input "
    "?? 'Input not available')}"
)

old_expected = (
    "{examples[selected]?.output??"
    "'Not supplied in question examples'}"
)

new_expected = (
    "{typeof visibleTests[selected]==='object' "
    "&& visibleTests[selected]!==null "
    "? ((visibleTests[selected] as PublicCase).expected "
    "?? 'Expected output not yet configured') "
    ": (examples[selected]?.output "
    "?? 'Expected output not available')}"
)

if old_input not in panel or old_expected not in panel:
    sys.exit(
        "ERROR: Testcase JSX differs from the "
        "expected version. No files changed."
    )

panel = panel.replace(old_input, new_input, 1)
panel = panel.replace(old_expected, new_expected, 1)

panel = panel.replace(
    "These are problem examples. "
    "The grader may use different input values. "
    "Private test cases are never disclosed.",
    "Verified public test cases are shown above. "
    "Private test inputs and expected outputs "
    "are never disclosed."
)

# ---------------------------------------------
# 3. Validate and back up
# ---------------------------------------------

compile(main, str(main_file), "exec")

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = root / f"backup_public_cases_{stamp}"
backup.mkdir()

(backup / "main.py").write_text(
    main_file.read_text(encoding="utf-8-sig"),
    encoding="utf-8"
)

(backup / "JudgePanel.tsx").write_text(
    panel_file.read_text(encoding="utf-8-sig"),
    encoding="utf-8"
)

# ---------------------------------------------
# 4. Install updates
# ---------------------------------------------

main_file.write_text(main, encoding="utf-8")
panel_file.write_text(panel, encoding="utf-8")

print("SUCCESS: Public test case UI updated.")
print("Backup location:", backup)
print("Backend API now supplies input and expected.")
print("JudgePanel now renders structured test cases.")
print("Hidden tests remain private.")