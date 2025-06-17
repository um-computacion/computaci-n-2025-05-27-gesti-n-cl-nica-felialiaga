import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from modelo.Turnosclinica import Paciente, Medico, Turno, Receta, HistoriaClinica, Clinica, Especialidad
from modelo.excepciones import ErrorPaciente, ErrorMedico, EspecialidadYaExistente, RecetaInvalidaException

class TestClasesPrincipales(unittest.TestCase):

    def test_agregar_paciente_y_medico(self):
        clinica = Clinica()
        paciente = Paciente("Ana", "Gomez", "12345678", "01/01/1990")
        clinica.agregar_paciente(paciente)

        self.assertIn("12345678", clinica.obtener_pacientes())

        especialidad = Especialidad("Cardiologia", ["lunes", "miércoles"])
        medico = Medico("Luis", "Perez", "1111", [especialidad])
        clinica.agregar_medico(medico)

        self.assertIn("1111", clinica.obtener_medicos())

    def test_no_agregar_paciente_duplicado(self):
        clinica = Clinica()
        paciente = Paciente("Ana", "Gomez", "12345678", "01/01/1990")
        clinica.agregar_paciente(paciente)
        with self.assertRaises(ErrorPaciente):
            clinica.agregar_paciente(paciente)

    def test_no_agregar_medico_duplicado(self):
        clinica = Clinica()
        especialidad = Especialidad("Cardiologia", ["lunes"])
        medico = Medico("Luis", "Perez", "1111", [especialidad])
        clinica.agregar_medico(medico)
        with self.assertRaises(ErrorMedico):
            clinica.agregar_medico(medico)

    def test_agregar_especialidad_a_medico(self):
        especialidad = Especialidad("Cardiologia", ["lunes"])
        medico = Medico("Luis", "Perez", "1111", [especialidad])
        nueva_especialidad = Especialidad("Clinica", ["martes"])
        medico.agregar_especialidad(nueva_especialidad)

        self.assertEqual(len(medico._Medico__especialidades), 2)

    def test_evitar_especialidad_duplicada(self):
        especialidad = Especialidad("Cardiologia", ["lunes"])
        medico = Medico("Luis", "Perez", "1111", [especialidad])
        with self.assertRaises(EspecialidadYaExistente):
            medico.agregar_especialidad(especialidad)

    def test_emitir_receta_valida(self):
        clinica = Clinica()
        paciente = Paciente("Ana", "Gomez", "12345678", "01/01/1990")
        especialidad = Especialidad("Clinica", ["lunes"])
        medico = Medico("Luis", "Perez", "1111", [especialidad])
        clinica.agregar_paciente(paciente)
        clinica.agregar_medico(medico)
        clinica.emitir_receta("12345678", "1111", ["Paracetamol"])
        historia = clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_sin_medicamentos(self):
        clinica = Clinica()
        paciente = Paciente("Ana", "Gomez", "12345678", "01/01/1990")
        especialidad = Especialidad("Clinica", ["lunes"])
        medico = Medico("Luis", "Perez", "1111", [especialidad])
        clinica.agregar_paciente(paciente)
        clinica.agregar_medico(medico)
        with self.assertRaises(RecetaInvalidaException):
            clinica.emitir_receta("12345678", "1111", [])

if __name__ == '__main__':
    unittest.main()
