from pathlib import Path


class Resource:
    _BASE_DIR_NAME = 'resources'
    _BASE_DIR_PATH = Path(__file__).parent / _BASE_DIR_NAME

    def __init__(self, name: str):
        self.path = Resource._BASE_DIR_PATH / name

        if not self.path.exists():
            raise ValueError(f'Resource "{name}" not found!')

        if not (self.path.is_file() or self.path.is_dir()):
            raise ValueError(f'Invalid type of resource "{name}"!')

    def __repr__(self):
        return str(self.path)

    def pyinstaller_dst(self) -> str:
        if self.path.is_dir():
            return str(Path(Resource._BASE_DIR_NAME) / self.path.name)
        else:
            return str(Path(Resource._BASE_DIR_NAME) / '.')

    @staticmethod
    def get_all():
        for resource_path in Resource._BASE_DIR_PATH.iterdir():
            try:
                yield Resource(resource_path.name)
            except Exception:
                pass
