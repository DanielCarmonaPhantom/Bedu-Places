class Image():
    def __init__(self, id, usuario, image):
        self.id = id
        self.usuario = usuario
        self.image = image

    def to_JSON(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'url_imagen': self.image
        }