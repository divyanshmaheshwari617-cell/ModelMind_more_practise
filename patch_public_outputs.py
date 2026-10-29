from pathlib import Path
import shutil
p=Path('backend/main.py')
if not p.exists():raise SystemExit('Run from the ModelMind project root. Missing backend/main.py')
s=p.read_text(encoding='utf-8')
needle='    for test_name, test_function in test_items:\n'
if 'public_case_specs =' in s:raise SystemExit('Public output diagnostics already applied.')
if needle not in s:raise SystemExit('Runner structure differs. Backend unchanged; do not apply blindly.')
# Added inside generated runner string. Only documented simple pure-function samples; never report synthetic outputs for other questions.
insert='''    # Diagnostics only for verified, simple public cases. Other questions retain no comparison.
    public_case_specs = {{
        "Mean with normal values": ("calculate_mean", [1, 2, 3, 4, 5], 3.0),
        "Mean with negative values": ("calculate_mean", [-5, 5], 0.0),
        "Sum even mixed": ("sum_even", [1, 2, 3, 4, 5, 6], 12),
        "All odd numbers": ("sum_even", [1, 3, 5], 0),
    }}

'''
s=s.replace(needle,insert+needle,1)
# Insert after every test iteration, before score block; note this runs func again only for four simple pure functions.
marker='    # -----------------------------------------------------\n    # Score\n'
addition='''        if len(result["tests"]) <= 2 and test_name in public_case_specs:
            fn_name, sample_input, sample_expected = public_case_specs[test_name]
            detail = {{"input": f"numbers = {{sample_input!r}}", "expected": repr(sample_expected)}}
            try:
                detail["actual"] = repr(namespace[fn_name](sample_input))
            except Exception as exc:
                detail["actual"] = f"{{type(exc).__name__}}: {{exc}}"
            result["tests"][-1].update(detail)

'''
if marker not in s:raise SystemExit('Score section differs. Backend unchanged.')
s=s.replace(marker,addition+marker,1)
backup=p.with_suffix('.py.before_lc_ui_backup')
shutil.copy2(p,backup)
p.write_text(s,encoding='utf-8')
print('Patched',p,'Backup:',backup)
