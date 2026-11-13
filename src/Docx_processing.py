import os
from Delegate_list import Delegate
from docxtpl import DocxTemplate
import datetime as dt


def docx_process(delegate_list, tpl_route, dest_directory, firmante):
    """
    A esta función se le pasa una lista de objetos Delegate con una serie de atributos para poder generar documentos
    automatizados, se le pasa la ruta de la plantilla que se va a usar, la ruta de de la carpeta de destino y un string
    con el nombre del firmante del documento.
    """
    for deleg in delegate_list:
        doc = DocxTemplate(tpl_route)

        context = {
            "{nombre}": deleg.name,
            "{apellidos}": deleg.surname,
            "{fecha_larga}": dt.datetime.today().strftime("%d de %B de %Y"),
            "{fecha_corta}": dt.datetime.today().strftime("%d-%m-%Y"),
            "{firmante}": firmante
            }

        doc.render(context)
        save_route = os.path.join(dest_directory, f"{deleg.name}.docx")
        doc.save(save_route)

def get_delegates():
    return [
    Delegate("María", "Fernández Ortega", "nato", "Presidenta", ["Representante de estudiantes"], ["Asamblea Universitaria"], [], ["Ingeniería", "Ciencias"], 4, ["Secretaria de actas", "Tesorera"]),
    Delegate("Carlos", "Ramírez Soto", "de integración", "Vicepresidente", [], [], ["Consejo de Departamento de Física"], ["Ciencias"], 2, ["Vocal"]),
    Delegate("Lucía", "Gómez Navarro", "de grupo", "Secretaria", ["Junta de Escuela de Arquitectura"], ["CEST"], ["Consejo de Departamento de Diseño"], ["Arquitectura"], 3, []),
    Delegate("Javier", "Morales Pérez", "nato", "Tesorero", ["Junta de Escuela de Informática", "Comisión de Docencia"], [], [], ["Informática", "Telecomunicaciones"], 5, ["Presidente", "Vicepresidente"]),
    Delegate("Ana", "Castillo Rivas", "de grupo", "", [], [], [], ["Humanidades"], 0, []),
    Delegate("Pablo", "Herrera Díaz", "de integración", "Vocal", ["Junta de Escuela de Industriales"], ["Asamblea Universitaria", "CEST"], ["Consejo de Departamento de Mecánica"], ["Ingeniería"], 6, ["Secretario", "Coordinador de comisiones"]),
    Delegate("Sofía", "Vargas Luna", "nato", "Presidenta", [], ["Claustro"], [], ["Medicina", "Enfermería"], 1, []),
    Delegate("Diego", "Ruiz Medina", "de grupo", "Vicepresidente", ["Junta de Escuela de Económicas"], [], ["Consejo de Departamento de Contabilidad"], ["Economía"], 2, ["Tesorero"]),
    Delegate("Elena", "Santos Cabrera", "de integración", "Secretaria", ["Junta de Escuela de Derecho"], ["Asamblea Universitaria"], [], ["Derecho", "Ciencias Políticas"], 7, ["Presidenta", "Vocal", "Representante de claustro"]),
    Delegate("Andrés", "Molina Quintero", "nato", "Vocal", [], ["CEST", "Claustro"], ["Consejo de Departamento de Química", "Consejo de Departamento de Biología"], ["Ciencias", "Biotecnología"], 3, ["Coordinador de deportes"]),
]

if __name__ == "__main__":
    deleg_list = get_delegates()
    tpl_route = r"C:\Users\Kairo\Desktop\Automatizacion\Plantillas\20240319_justificacion_faltareunion.docx"
    dest_directory = r"C:\Users\Kairo\Desktop\Automatizacion\Pruebas"
    firmante = "Muhammad Ruano Horofichi"
    docx_process(deleg_list, tpl_route, dest_directory, firmante)
    print("DONE")
         
    