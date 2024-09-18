import json

class Manager():
    @staticmethod
    def create_tracker(filename):
        with open(filename, mode="w", encoding="utf-8") as write_file:
            json.dump([], write_file)

    @staticmethod
    def json_append(filename, new_data):
        with open(filename, 'r+', encoding="utf-8") as file:
            file_data = json.load(file)
            file_data.append(new_data)
            file.seek(0)
            json.dump(file_data, file)

    @staticmethod
    def json_load(filename):
        with open(filename, mode='r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_write(filename, data):
        with open(filename, mode='w', encoding="utf-8") as json_file:
            json.dump(data, json_file)

    @staticmethod
    def generate_id(filename):
        data = Manager.json_load(filename)
        if len(data) == 0:
            return 1
        for elem in data:
            previous_id = elem["id"]
        return previous_id + 1

    @staticmethod
    def json_pretty_print(data):
        return json.dumps(data, indent=0)
