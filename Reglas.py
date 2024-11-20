"""
Este archivo define las reglas de negocio del sistema. Contiene:
- Clases para manejar Atletas, Disciplinas, Eventos, Participaciones y la Controladora Olimpiada.
- Gestiona la lógica principal: búsqueda, asignaciones, validaciones y persistencia.
"""

from datetime import date

class Disciplina:
    def __init__(self,cod,nom):
        self.id_disciplina = cod
        self.nombre = nom

class Atleta:
    def __init__(self,id_doc,nom,sex,pais):
        self.id_atleta = id_doc
        self.nombre_completo = nom
        self.sexo = sex
        self.pais = pais
        self.disciplina = None #Inicialmente, el atleta no tiene Disciplina asignada.

    def asignar_disciplina(self,disciplina):
        if self.disciplina != disciplina:
            self.disciplina = disciplina #Asigna una nueva Disciplina si no es la actual.
            return True
        return False #Retorna False si la Disciplina ya estaba asignada.

class Evento:
    def __init__(self,cod,nom_prueba,disc,fecha_ini,fecha_fin):
        self.id_evento = cod
        self.nombre_prueba = nom_prueba
        self.disciplina = disc
        self.fecha_inicio = fecha_ini
        self.fecha_fin = fecha_fin
        self.participaciones = [] #Lista de participaciones del evento.

    def agregar_participacion(self,participacion):
        #Agrega una participación al Evento si aún no existe.
        if participacion not in self.participaciones:
            self.participaciones.append(participacion)
            return True
        return False

class Participacion:
    def __init__(self,atl,ev,puntaje):
        self.atleta = atl
        self.evento = ev
        self.puntaje = puntaje

class Olimpiada:
    #Clase Controladora
    def __init__(self):
        # Datos de prueba para atletas
        self.lista_atletas = [
            Atleta(1234, "Juán López", "M", "Argentina"),
            Atleta(5678, "María Gómez", "F", "Chile"),
            Atleta(9101, "Marcos Rodríguez", "M", "Uruguay")
        ]
        #Datos de prueba para disciplinas
        self.lista_disciplinas = [
            Disciplina(1, "Fútbol"),
            Disciplina(2, "Atletismo")
        ]
        #Asigna disciplinas a los atletas de prueba
        self.lista_atletas[0].asignar_disciplina(self.lista_disciplinas[0])  #Juán -> Fútbol
        self.lista_atletas[1].asignar_disciplina(self.lista_disciplinas[1])  #María -> Atletismo
        self.lista_atletas[2].asignar_disciplina(self.lista_disciplinas[0])  #Marcos -> Fútbol
       
        #Datos de prueba para eventos
        self.lista_eventos = [
            Evento(201, "Partido Inaugural", self.lista_disciplinas[0], date(2024, 7, 24), date(2024, 7, 24)),
            Evento(202, "Salto de Longitud", self.lista_disciplinas[1], date(2024, 8, 3), date(2024, 8, 4))
        ]

    def agregar_atleta(self,nom,sex,id_atl,pais):
        #Asigna una Disciplina al Atleta sino la tiene asignada aún.
        if not self.buscar_atleta(id_atl):
            nuevo_atleta = Atleta(id_atl, nom, sex, pais)
            self.lista_atletas.append(nuevo_atleta)
            return True
        return False

    def buscar_atleta(self,id_atl):
        for atl in self.lista_atletas:
            if atl.id_atleta == id_atl:
                return atl #Retorna información del Atleta si lo encuentra.
        return None

    def agregar_evento(self,cod_event,nom_prueba,cod_disc,fecha_ini,fecha_fin):
        #Verifica que no exista otro Evento con el mismo nombre.
        for evento in self.lista_eventos:
            if evento.nombre_prueba == nom_prueba:
                return False

        #Busca la disciplina por su ID
        disc = self.buscar_disciplina(cod_disc)
        if disc:
            #Si la Disciplina existe, crea y agrega el nuevo Evento.
            nuevo_evento = Evento(cod_event, nom_prueba, disc, fecha_ini, fecha_fin)
            self.lista_eventos.append(nuevo_evento)
            return True
        return False #Retorna False si la Disciplina no existe.

    def buscar_disciplina(self,cod_disc):
        for disc in self.lista_disciplinas:
            if disc.id_disciplina == cod_disc:
                return disc #Retorna la Disciplina si la encuentra.
        return None

    def asignar_disciplina_atleta(self,id_atl,cod_disc):
        atl = self.buscar_atleta(id_atl)
        disc = self.buscar_disciplina(cod_disc)
        if atl and disc:
            return atl.asignar_disciplina(disc) #Asigna la Disciplina al Atleta si ambos existen.
        return False

    def registrar_participacion(self,cod_event,id_atl,puntaje):
        evento = self.buscar_evento(cod_event)
        atleta = self.buscar_atleta(id_atl)
        if evento and atleta and atleta.disciplina == evento.disciplina:
            participacion = Participacion(atleta, evento, puntaje)
            return evento.agregar_participacion(participacion) #Registra Participación si cumple que exista Evento, Atleta y que Disciplina coincida con Disciplina del Evento.
        return False

    def buscar_evento(self,cod_event):
        for evento in self.lista_eventos:
            if evento.id_evento == cod_event:
                return evento #Retorna el Evento si lo encuentra.
        return None