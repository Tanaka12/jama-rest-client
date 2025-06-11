
import json

ITEMS_COUNT: int = 30

if __name__ == "__main__":

    result = \
    {
        "meta": {
            "status": "OK",
            "timestamp": "2025-05-26T16:11:23.071+0000",
            "pageInfo": {
                "startIndex": 0,
                "resultCount": 0,
                "totalResults": 0
            }
        },
        "links": {
            "data.createdBy": {
                "type": "users",
                "href": "createdBy"
            },
            "data.fields.user1": {
                "type": "users",
                "href": "user1"
            },
            "data.modifiedBy": {
                "type": "users",
                "href": "modifiedBy"
            },
            "data.fields.projectManager": {
                "type": "users",
                "href": "projectManager"
            },
            "data.fields.projectGroup": {
                "type": "picklistoptions",
                "href": "projectGroup"
            },
            "data.parent": {
                "type": "projects",
                "href": "parent"
            },
            "data.fields.statusId": {
                "type": "picklistoptions",
                "href": "statusId"
            }
        }
    }

    data = []
    for index in range(1, ITEMS_COUNT):
        element = \
        {
            'id': index,
            'projectKey': f'DummyProjectKey {index}',
            'parent': index + 1,
            'isFolder': True,
            'createdDate': '2020-02-20T12:50:26.000+0000',
            'modifiedDate': '2020-02-20T12:50:26.000+0000',
            'createdBy': index + 2,
            'modifiedBy': index + 3,
            'fields':
            {
                'randomFieldStr': 'randomFieldStr',
                'randomFieldBool': True,
                'randomFieldInt': 1
            }
        }

        data.append(element)

    result['data'] = data

    with open('file.json', 'w') as file_handle:
        file_handle.write(json.dumps(result))
