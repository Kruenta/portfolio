import ezdxf

msp = ezdxf.readfile("2627 ВЛ-0,4кВ от КТП 463 ф.27 ПС Володаровка23.dxf").modelspace()


# not_dashed_entities = ezdxf.query.EntityQuery
# blockrefs = msp.query('INSERT[name=="BL2"]')
# print(blockrefs)

def get_catalog(points):
    catalog = []
    for i in points:
        current = {
            'X': "",
            'Y': "",
            "Name": ""
        }
        catalog.append(current)
    return catalog


for e in msp.query('INSERT[name=="BL2"]'):
    # catalog = get_catalog(e.dxf._entity._sub_entities)
    # print(catalog)
    for i in e.dxf._entity._sub_entities:
        # print(e.dxf._entity._sub_entities.__dict__)
        print(i.dxf.__dict__)
