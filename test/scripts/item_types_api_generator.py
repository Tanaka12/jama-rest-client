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
            'image': '',
            'category': f'DummyCategory {index}',
            'fields': [],
            'system': True,
            'type': 'itemtypes',
            'fields': [
                {
                    'id': 1,
                    'name': 'DummyName 1',
                    'label': 'DummyLabel 1',
                    'fieldType': 'DummyFieldType 1',
                    'readOnly': False,
                    'required': False,
                    'triggerSuspect': False,
                    'synchronize': True,
                    'textType': 'DummyTextType 1'
                }
            ]
        }

        data.append(element)

    result['data'] = data

    print(json.dumps(result))
