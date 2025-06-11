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
            'fileName': f'DummyFileName {index}',
            'mimeType': f'DummyMimeType {index}',
            'fileSize': index,
            'id': index + 1,
            'documentKey': f'DummyDocumentKey {index}',
            'globalId': f'DummyGlobalId {index}',
            'project': index + 2,
            'itemType': index + 3,
            'createdDate': '2020-02-20T12:50:26.000+0000',
            'modifiedDate': '2020-02-20T12:50:26.000+0000',
            'lastActivityDate': '2020-02-20T12:50:26.000+0000',
            'createdBy': index + 4,
            'modifiedBy': index + 5,
            'fields': {
                'fieldStr': 'DummyField',
                'fieldInt': 0,
                'fieldBool': True
            },
            'resources': {
                'self': {
                    'allowed': [
                        'GET',
                        'PUT',
                        'PATCH',
                        'DELETE'
                    ]
                }
            },
            'lock': {
                'locked': False,
                'lastLockedDate': '2020-02-20T12:50:26.000+0000',
                'lockedBy': 0
            }
        }

        data.append(element)

    result['data'] = data

    with open('file.json', 'w') as file_handle:
        file_handle.write(json.dumps(result))
