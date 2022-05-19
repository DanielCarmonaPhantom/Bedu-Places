from flask import Blueprint, jsonify


# Models
from models.ImageModels import ImagenModel


main=Blueprint('image_blueprint',__name__)

@main.route('/')
def get_imagenes():
    try:
        images = ImagenModel.get_images()
        return jsonify(images)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500