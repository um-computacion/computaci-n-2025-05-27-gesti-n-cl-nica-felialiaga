import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from modelo.Turnosclinica import validar_existencia_paciente, validar_existencia_medico, validar_turno_no_duplicado, obtener_dia_semana_en_espanol, validar_especialidad_en_dia
from modelo.excepciones import TurnoOcupadoException, MedicoNoDisponibleExcepcion, ErrorPaciente, ErrorMedico
from modelo.Turnosclinica import Medico, Turno, Paciente, Especialidad

class TestValidaciones(unittest.TestCase):

    def setUp(self):
        
        self.pacientes = {
            "12345678": Paciente("Juan", "Perez", "12345678", "01/01/1990"),
        }

        self.medicos = {
            "1111": Medico("Ana", "Lopez", "1111", [Especialidad("Cardiologia", ["lunes", "martes"])]),
        }

        self.turnos = []
       
        paciente = self.pacientes["12345678"]
        medico = self.medicos["1111"]
        especialidad = medico.obtener_especialidad_para_dia("lunes")
        fecha_hora = "01/07/2025 10:00"
        turno_existente = Turno(paciente, medico, fecha_hora, especialidad)
        self.turnos.append(turno_existente)

    def test_validar_existencia_paciente_ok(self):
       
        validar_existencia_paciente(self.pacientes, "12345678")

    def test_validar_existencia_paciente_error(self):
        with self.assertRaises(ErrorPaciente):
            validar_existencia_paciente(self.pacientes, "99999999")

    def test_validar_existencia_medico_ok(self):
        validar_existencia_medico(self.medicos, "1111")

    def test_validar_existencia_medico_error(self):
        with self.assertRaises(ErrorMedico):
            validar_existencia_medico(self.medicos, "2222")

    def test_validar_turno_no_duplicado_error(self):
   
        from modelo.Turnosclinica import validar_turno_no_duplicado as vtn

        class StubTurnos:
            def __init__(self, turnos):
                self.__turnos = turnos
            def validar_turno_no_duplicado(self, matricula, fecha_hora):
                fecha = datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M")
                for t in self.__turnos:
                    if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha:
                        raise TurnoOcupadoException("El turno ya esta ocupado.")

        stub = StubTurnos(self.turnos)

        with self.assertRaises(TurnoOcupadoException):
            stub.validar_turno_no_duplicado("1111", "01/07/2025 10:00")

    def test_obtener_dia_semana_en_espanol(self):
       
        from modelo.Turnosclinica import obtener_dia_semana_en_espanol
        dia = obtener_dia_semana_en_espanol("01/07/2025 10:00")
        self.assertEqual(dia, "martes")

    def test_validar_especialidad_en_dia_ok(self):
      
        from modelo.Turnosclinica import validar_especialidad_en_dia
        validar_especialidad_en_dia(self.medicos["1111"], "Cardiologia", "lunes")

    def test_validar_especialidad_en_dia_error(self):
        from modelo.Turnosclinica import validar_especialidad_en_dia
        with self.assertRaises(MedicoNoDisponibleExcepcion):
            validar_especialidad_en_dia(self.medicos["1111"], "Cardiologia", "domingo")

if __name__ == "__main__":
    unittest.main()
