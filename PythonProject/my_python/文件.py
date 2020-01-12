import sys, getopt
import csv
import json
from ast import literal_eval

def main(argv):
    pretty = False
    try:
        opts, args = getopt.getopt(argv,"hp")
    except getopt.GetoptError:
        print('test.py [-p]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py [-p]')
            sys.exit()
        elif opt == '-p':
            pretty = True

    data = read_csv("学生信息表.csv")
    #print(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
    write_json(data, "test.json", pretty)


def read_csv(file):
    csv_rows = {}

    def format(source):
        try:
            source = literal_eval(source)
        except:
            pass
        finally:
            return source

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows[format(row[title[0]])] = {title[i]:format(row[title[i]]) for i in range(len(title)) if not title[i].startswith('_')}

    return csv_rows


def write_json(data, json_file, format = True):
    with open(json_file, "w") as f:
        if format:
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))

if __name__ == "__main__":
    main(sys.argv[1:])