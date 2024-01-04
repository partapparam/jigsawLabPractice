from artist import Artist


class ArtistAdapter:
    def select_attributes(self, artist):
        return {'name': artist['name'], 
                'popularity': artist['popularity'],
                'id': artist['id']
                }
    
    def run(self, artists):
        artists = []
        for artist in artists:
            artist_attrs = self.select_attributes(artist)
            artist_obj = Artist(**artist_attrs)
            artists.append(artist_obj)
        return artists
