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
            'documentKey': f'DummyDocumentKey {index}',
            'globalId': f'DummyGlobalId {index}',
            'itemType': index + 1,
            'project': index + 2,
            'createdDate': f'DummyCreatedDate {index}',
            'modifiedDate': f'DummyModifiedDate {index}',
            'lastActivityDate': f'DummyLastActivityDate {index}',
            'createdBy': index + 3,
            'modifiedBy': index + 4,
            "fields": {
                "fieldStr": "DummyField",
                "fieldInt": 0,
                "fieldBool": True
            },
            "resources": {
                "self": {
                    "allowed": [
                        "GET",
                        "PUT",
                        "PATCH",
                        "DELETE"
                    ]
                }
            },
            "location": {
                "sortOrder": index,
                "globalSortOrder": index + 1,
                "sequence": f'DummySequence {index}',
                "parent": {
                    "item": 0
                }
            },
            "lock": {
                "locked": bool(index % 2),
                "lastLockedDate": f'DummyLastLockedDate {index}'
            },
            "type": "items"
        }

        data.append(element)

    result['data'] = data

    print(json.dumps(result))
