"""Not ABC because not all the methods are required everywhere."""

class BaseRepository:
    def create(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError

    def list(self, *args, **kwargs):
        raise NotImplementedError
