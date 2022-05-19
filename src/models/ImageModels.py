from database.db import get_connection
from .entities.Image import Image

class ImagenModel():
    @classmethod
    def get_images(self):
        try:
            connection = get_connection()
            images = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario, image FROM lugares")
                resultset = cursor.fetchall()

                for row in resultset:
                    image = Image(row[0], row[1], row[2])
                    images.append(image.to_JSON())

            connection.close()
            return images

        except Exception as ex:
            raise Exception(ex)