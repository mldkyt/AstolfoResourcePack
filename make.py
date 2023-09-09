import os
import zipfile

def recursive_folder(path):
  # Recursive function to add all files in a folder and subfolders
  for file in os.listdir(path):
    if os.path.isdir(path + '/' + file):
      print('Recursively searching ' + path + '/' + file)
      recursive_folder(path + '/' + file)
    else:
      print('Adding ' + path + '/' + file)
      pack.write(path + '/' + file)

# delete Astolfo2.zip
if os.path.exists('Astolfo2.zip'):
  os.remove('Astolfo2.zip')
# Create a zip file from folder assets, and files pack.png, pack.mcmeta
with zipfile.ZipFile('Astolfo2.zip', 'w') as pack:
  print('Adding pack.mcmeta')
  pack.write('pack.mcmeta')
  print('Adding pack.png')
  pack.write('pack.png')
  recursive_folder('assets')


with zipfile.ZipFile('Astolfo2mod.jar', 'w') as jarmod:
  jarmod.write('assets/minecraft/textures/gui/title/mojangstudios.png')
