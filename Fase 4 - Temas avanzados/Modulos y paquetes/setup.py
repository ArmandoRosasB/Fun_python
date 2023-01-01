from setuptools import setup


# Set up paquetes
setup(
    name = 'Mensajes',
    version= '2.0',
    description= 'Un paquete para saludar y despedir',
    author= 'Jose Armando Rosas Balderas',
    author_email= 'armando.rosas133@gmail.com',
    url= 'https://github.com/ArmandoRosasB',
    packages= ['Mensajes', 'Mensajes.Bienvenidas', 'Mensajes.Despedidas'],
    scripts= ['test.py']
)

# Para ejecutar el setup
# Generar el distribuible

# Cargar los pauetes en python o actaulizarlo
'''
py setup.py sdist

cd dist

pip install fileName.tar.gz

EN CASO DE ACTUALIZAR 
pip install newFileName.tar.gz --upgrade

pip list 

'''

# PARA DESINSTALAR

'''
pip uninstall nombrePaquete
'''