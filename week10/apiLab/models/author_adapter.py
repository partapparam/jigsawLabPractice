from models.author import Author


class AuthorAdapter:
    def select_attributes(self, author: dict) -> dict:
        name: str = author['name']
        id: str = author['key']
        work_count = author['work_count']
        return {'name': name, 
                'id': id,
                # 'top_work': top_work,
                'work_count': work_count
                }
    
    def run(self, authors: list[dict]) -> list[Author]:
        authors_list: list = []
        for author in authors:
            author_attrs:dict  = self.select_attributes(author=author)
            author_obj = Author(**author_attrs)
            authors_list.append(author_obj)
        return authors_list
