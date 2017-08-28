import os
import shutil

from cookiecutter import main
import pytest

CC_ROOT = os.path.abspath(
        os.path.join(
            __file__,
            os.pardir,
            os.pardir,
        )
)


@pytest.fixture(scope='function')
def default_baked_project(tmpdir):
    out_dir = str(tmpdir.mkdir('pki-project'))

    main.cookiecutter(
            CC_ROOT,
            no_input=True,
            # extra_content={},
            output_dir=out_dir,
    )

    yield os.path.join(
            out_dir,
            'acme_corp-pki',
    )

    shutil.rmtree(out_dir)


def test_readme(default_baked_project):
    readme_path = os.path.join(default_baked_project, 'README.md')

    assert os.path.exists(readme_path)
    assert no_curlies(readme_path)


def test_makefile(default_baked_project):
    makefile_path = os.path.join(default_baked_project, 'Makefile')

    assert os.path.exists(makefile_path)
    assert no_curlies(makefile_path)


def test_folders(default_baked_project):
    expected_dirs = [

    ]

    ignored_dirs = [
            default_baked_project,
    ]

    abs_expected_dirs = [os.path.join(default_baked_project, d) for d in expected_dirs]
    abs_dirs, _, _ = list(zip(*os.walk(default_baked_project)))

    assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0


def no_curlies(filepath):
    """
    Utility to ensure that no curly braces appear in a file
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
            '{{',
            '}}',
            '{%',
            '%}',
    ]

    template_strings_in_file = [s in data for s in template_strings]

    return not any(template_strings_in_file)
