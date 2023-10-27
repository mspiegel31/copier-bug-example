from pathlib import Path
import yaml
from .helpers import generate_project

def test_project_generates(
    tmp_path: Path,
) -> None:

    answers = {
        'project_name': 'test-project',
        'description': 'A test project',
        'use_pepperoni': True,
    }
    run_result = generate_project(tmp_path, answers)

    assert run_result[1] == 0
    expected_files = set(
        [
            tmp_path / ".copier-answers.yml",
            tmp_path / "order.yaml",
            tmp_path / "README.md",
        ]
    )
    actual_files = set(path for path in tmp_path.rglob("*") if path.is_file())
    assert actual_files == expected_files

def test_multi_select_example_works(
    tmp_path: Path,
) -> None:

    answers = {
        'project_name': 'test-project',
        'description': 'A test project',
        'use_pepperoni': True,
    }
    
    run_result = generate_project(tmp_path, answers)
    assert run_result[1] == 0
    
    with (tmp_path / "order.yaml").open('r') as f:
        order = yaml.safe_load(f)
    
    assert order['pizza']['toppings'] ==  ['pepperoni']
