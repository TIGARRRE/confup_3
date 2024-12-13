import yaml
import re
import argparse

def parse_yaml(yaml_string):
    try:
        data = yaml.safe_load(yaml_string)

        if any('@(undefined_constant)' in str(value) for value in data.values()):
            return None
        return data
    except yaml.YAMLError:
        return None

def resolve_constants(data):
    constants = data.get('app', {}).get('constants', {})
    
    def replace_constants(value):
        if isinstance(value, str):
          
            result = re.sub(r'@\((\w+)\)', lambda match: str(constants.get(match.group(1), match.group(0))), value)

            try:
                return int(result)
            except ValueError:
                return result  
        return value

    def process_data(data):
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = process_data(value)
        elif isinstance(data, list):
            for i in range(len(data)):
                data[i] = process_data(data[i])
        else:
            data = replace_constants(data)
        return data

    process_data(data)
    return data

def convert_to_custom_language(data):
    output = []
    
    def convert(data, indent=0):
        if not isinstance(data, dict):
            print(f"Ожидался словарь, но получен: {type(data).__name__}")
            return

        for key, value in data.items():
            line = ' ' * indent + f"{key} -> "
            if isinstance(value, dict):
                output.append(line + "{")
                convert(value, indent + 2)
                output.append(' ' * indent + "}")
            elif isinstance(value, str):  
                output.append(line + f"'{value}'")
            elif isinstance(value, (int, float)): 
                output.append(line + f"'{value}'")
            elif isinstance(value, bool):
                output.append(line + str(value).lower())
            else:
                print(f"Неизвестный тип значения: {value}")
                
    
    convert(data)
    return '\n'.join(output)

def main():

    parser = argparse.ArgumentParser(description='Обработка YAML конфигурации.')
    parser.add_argument('input_file', type=str, help='Путь к входному YAML файлу')
    parser.add_argument('output_file', type=str, help='Путь к выходному файлу для записи результата')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    with open(input_file, 'r', encoding='utf-8') as f:
        yaml_input = f.read()

    data = parse_yaml(yaml_input)

    if data is None or not isinstance(data, dict):
        print("Ошибка: данные должны быть в формате словаря.")
        return

    data = resolve_constants(data)

    custom_language_output = convert_to_custom_language(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(custom_language_output)

if __name__ == "__main__":
    main()