from jama_rest_client.model.item import Item

class ItemParser:

    @staticmethod
    def parse(item_dict: dict) -> Item:
        item: Item = Item()
        item.id = item_dict['id']
        item.document_key = item_dict['documentKey']
        item.type_id = item_dict['itemType']
        item.name = item_dict['fields']['name']

        return item