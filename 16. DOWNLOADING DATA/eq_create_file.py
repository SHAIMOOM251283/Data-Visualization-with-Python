from pathlib import Path
import json

class ReadableVersion:

    def __init__(self):
        self.file_path = 'eq_data/recent_eq.geojson'
        self.all_eq_data = None
        
    def read_data_as_a_string_and_convert_to_a_python_object(self):
        path = Path(self.file_path)
        contents = path.read_text(encoding="utf-8")
        self.all_eq_data = json.loads(contents)

    def create_a_more_readable_version_of_the_data_file(self):
        path = Path('eq_data/readable_recent_eq.geojson')
        readable_contents = json.dumps(self.all_eq_data, indent=4)
        path.write_text(readable_contents)

        print("--- File Created ---")
    
    def run(self):
        self.read_data_as_a_string_and_convert_to_a_python_object()
        self.create_a_more_readable_version_of_the_data_file()

if __name__ == '__main__':
    DataFile = ReadableVersion()
    DataFile.run()
