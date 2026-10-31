class Delegate:
    """
    Esta clase maneja los objetos que representan a cada delegado, el constructor se construyen todos los atributos
    necesarios para poder automatizar los documentos.  
    """
    def __init__(self, name, surname, position_del, position_jd, position_je, position_uni, position_cd, divisions, years_delegate, former_positions):
        """
        Los parámetros que tiene el objeto Delegate son: name, string del nombre; surname, string de los apellidos;
        position_del, un string que indica si se es nato, de integración o de grupo; position_jd, un string con el cargo
        de junta directiva; position_je, position_uni y position_cd son listas de strings de los cargos de junta de
        escuela, de la universidad (asamblea, cest, etc...) y de consejo departamento; years_delegate es un entero de
        los años que se lleva en delega; y former_positions una lista de strings con los cargos ejercidos anteriormente. 
        """
        self.name = name
        self.surname = surname
        self.position_del = position_del
        self.position_jd = position_jd
        self.position_je = position_je
        self.position_uni = position_uni
        self.position_cd = position_cd
        self.divisions = divisions
        self.years_delegate = years_delegate
        self.former_positions = former_positions