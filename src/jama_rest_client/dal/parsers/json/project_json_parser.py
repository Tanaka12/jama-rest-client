from datetime import datetime
from jama_rest_client.model.project import Project

class ProjectJSONParser:

    @staticmethod
    def parse(project_dict: dict) -> Project:
        project: Project = Project()
        project.id = project_dict['id']
        project.project_key = project_dict['projectKey']
        project.parent = project_dict['parent']
        project.is_folder = project_dict['isFolder']
        project.created_date = ProjectJSONParser.__parse_date_time(project_dict['createdDate'])
        project.modified_date = ProjectJSONParser.__parse_date_time(project_dict['modifiedDate'])
        project.created_by = project_dict['createdBy']
        project.modified_by = project_dict['modifiedBy']
        project.fields = project_dict['fields']

        return project
    
    @staticmethod
    def __parse_date_time(date_time: str) -> datetime:
        return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.000+0000')