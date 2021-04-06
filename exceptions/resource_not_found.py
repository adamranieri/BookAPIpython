class ResourceNotFound(Exception):

    description: str = 'Occurs when a resource is not found'

    def __init__(self,message: str):
        self.message = message

