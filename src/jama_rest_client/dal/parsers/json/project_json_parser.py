from jama_rest_client.model.project import Project

class ProjectJSONParser:

    @staticmethod
    def parse(project_dict: dict) -> Project:
        project: Project = Project()
        project.id = project_dict['id']
        project.project_key = project_dict['projectKey']
        project.is_folder = project_dict['isFolder']
        project.created_date = project_dict['createdDate']
        project.modified_date = project_dict['modifiedDate']
        project.created_by = project_dict['createdBy']
        project.modified_by = project_dict['modifiedBy']
        project.fields = project_dict['fields']

        return project