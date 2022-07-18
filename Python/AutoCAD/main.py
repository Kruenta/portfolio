import os

import ezdxf
import math

from openpyexcel import Workbook

files = os.listdir()

file_name = None

for file in files:
    if file.find('.dxf') != -1:
        file_name = file

if file_name is None:
    print('File not found')
    exit()

msp = ezdxf.readfile(file_name).modelspace()

catalog = {
    'points': [],
    'texts': [],
    'mowings': [],
    'finally': []
}


def get_distance(x1, x2, y1, y2):
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


for e in msp.query('INSERT[name=="BL2"]'):
    e = e.dxf
    point = {
        'lon': e.insert[0],
        'lat': e.insert[1]
    }
    catalog['points'].append(point)

    for i in e._entity._sub_entities:
        i = i.dxf
        text = {
            'lon': i.insert[0],
            'lat': i.insert[1],
            'text': i.text,
        }
        if text['text'] is None or text['text'] == '':
            catalog['mowings'].append(text)
        else:
            catalog['texts'].append(text)

points = []

for i in catalog['points']:
    distances = {}
    minimum = None
    for j in catalog['texts']:
        distance = get_distance(i['lon'], j['lon'], i['lat'], j['lat'])
        if minimum is None or distance < minimum:
            minimum = distance
            i['text'] = j['text']

# for i in catalog['points']:
#     print(i['text'] + ' ' + str(i['lat']) + ' ' + str(i['lon']))

removed = []

total = 0

for i in catalog['points']:
    catalog['finally'].append({
        'text': i['text'],
        'lat': i['lat'],
        'lon': i['lon'],
    })

    count = 0

    for j in catalog['points']:
        if j['text'] == i['text']:
            count += 1
            if count == 2 and i['text'] not in removed:
                catalog['finally'].append({
                    'text': 'укос',
                    'lat': j['lat'],
                    'lon': j['lon'],
                })

                total += 1
                removed.append(j['text'])

catalog = catalog['finally'][:-total]

output = open('cords.txt', 'w')
outlines = []

wb = Workbook()
ws = wb.active

for i in catalog:
    ws.append([i['text'], i['lat'], i['lon']])
    outlines.append(str(i['lat']) + "\t" + str(i['lon']))

dims = {}
for row in ws.rows:
    for cell in row:
        if cell.value:
            dims[cell.column] = max((dims.get(cell.column, 0), len(str(cell.value))))
for col, value in dims.items():
    if value < 3:
        ws.column_dimensions[col].width = 5
    else:
        ws.column_dimensions[col].width = value * 1.5

output.write("\n".join(outlines))
output.close()
wb.save('cords.xlsx')