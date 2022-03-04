from PIL import Image, ImageSequence
import os

while True:
    fotoPath = input('Path: ')

    fotos = os.listdir(fotoPath)

    print('Converting images...')

    # Get all images in directory
    for foto in fotos:
        if '.webp' in foto:

            # Open image
            im = Image.open(f'{fotoPath}\{foto}')

            # Check if image is GIF and save
            index = 0
            for f in ImageSequence.Iterator(im):
                index += 1
            if index > 1:
                im.info.pop('background', None)
                fotoJPG = foto.replace('.webp','') + '.gif'
                im.save(f'{fotoPath}\{fotoJPG}', 'gif', save_all=True)
            
            # Save iimage as JPEG
            else:
                im = im.convert('RGB')
                fotoJPG = foto.replace('.webp','') + '.jpg'
                im.save(f'{fotoPath}\{fotoJPG}', 'jpeg')

            os.remove(f'{fotoPath}\{foto}')
    
    print('Done!')

    again = input('Convert new album (Y/N): ')
    if again.lower() == 'n':
        break
    else:
        os.system('cls')
