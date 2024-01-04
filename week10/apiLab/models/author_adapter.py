from models.author import Author


class AuthorAdapter:
    def select_attributes(self, author):
        return {'name': author['name'], 
                'birth_date': author['birth_date'],
                'id': author['id'],
                'top_work': author['top_work'],
                'work_count': author['work_count']
                }
    
    def run(self, authors):
        authors_list = []
        for author in authors:
            author_attrs = self.select_attributes(author)
            author_obj = Author(**author_attrs)
            authors_list.append(author_obj)
        return authors_list
