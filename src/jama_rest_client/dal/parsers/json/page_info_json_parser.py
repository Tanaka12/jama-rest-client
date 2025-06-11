from jama_rest_client.model.page_info import PageInfo

class PageInfoJSONParser:

    @staticmethod
    def parse(page_info_dict: dict) -> PageInfo:
        page_info: PageInfo = PageInfo()
        page_info.result_count = page_info_dict['resultCount']
        page_info.start_index = page_info_dict['startIndex']
        page_info.total_results = page_info_dict['totalResults']

        return page_info
