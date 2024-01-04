from models.author import Author


class AuthorAdapter:
    def select_attributes(self, author):
        name = author['name']
        id = author['key']
        # top_work = author['top_work'] if author['top_work'] == None else ''
        work_count = author['work_count']
        return {'name': name, 
                'id': id,
                # 'top_work': top_work,
                'work_count': work_count
                }
    
    def run(self, authors):
        authors_list = []
        for author in authors:
            author_attrs = self.select_attributes(author)
            author_obj = Author(**author_attrs)
            authors_list.append(author_obj)
        return authors_list
