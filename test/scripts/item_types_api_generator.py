import json

ITEMS_COUNT: int = 30

if __name__ == "__main__":

    result = \
    {
        "meta": {
        "status": "OK",
        "timestamp": "2025-05-22T15:46:31.191+0000",
        "pageInfo": {
            "startIndex": 0,
            "resultCount": 0,
            "totalResults": 0
        }
        },
        "links": {
            "data.fields.pickList": {
                "type": "picklists",
                "href": ""
            },
            "data.fields.itemType": {
                "type": "itemtypes",
                "href": ""
            }
        }
    }

    data = []
    for index in range(1, ITEMS_COUNT):
        element = \
        {
            'id': index,
            'typeKey': f'DummyTypeKey {index}',
            'display': f'DummyDisplay {index}',
            'displayPlural': f'DummyDisplayPlural {index}',
            'description': f'DummyDescription {index}',
            'image': f'DummyImage {index}',
            'category': 'COMPONENT',
            'fields': [
                {
                    'id': 1,
                    'name': 'DummyName 1',
                    'label': 'DummyLabel 1',
                    'fieldType': 'ACTIONS',
                    'readOnly': False,
                    'readOnlyAllowApiOverwrite': False,
                    'required': False,
                    'triggerSuspect': False,
                    'synchronize': False,
                    'pickList': 1,
                    'textType': 'ATTACHMENT',
                    'itemType': 1
                }
            ],
            'system': True
        }

        data.append(element)

    result['data'] = data

    with open('file.json', 'w') as file_handle:
        file_handle.write(json.dumps(result))

