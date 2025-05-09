from pathlib import Path
import os
import json


def runner(output_file='./extracted_data.json'):
    env_vars = dict(os.environ)

    file_paths = []
    for path in Path('/').rglob('*'):
        try:
            if path.is_file():
                file_paths.append(str(path))
        except Exception as e:
            print(e)

    data = {
        'environment_variables': env_vars,
        'file_paths': file_paths
    }

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f'Data successfully extracted to {output_file}')
