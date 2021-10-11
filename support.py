from os import walk
import pygame

def import_folder(path, resize = False, size = (32, 32)):
    images = []

    for _, _, image_files in walk(path):
        for image in image_files:
            image_path = path + "/" + image
            img = pygame.image.load(image_path).convert_alpha()
            if resize:
                img = pygame.transform.scale(img, size)
            images.append(img)

    return images