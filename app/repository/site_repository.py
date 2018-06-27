from .repository_factory import Repository

class SiteRepository(Repository) :

    def save_site(self, data):
        self.save(data)
        return data