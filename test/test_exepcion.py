import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from modelo.excepciones import (
    PacienteNoEncontradoExcepcion,
    MedicoNoEncontrado,
    MedicoNoDisponibleExcepcion,
    TurnoOcupadoException,
    RecetaInvalidaException,
    ErrorAlAgregarPaciente,
    ErrorAlAgregarMedico,
    EspecialidadYaExistente,
)

class TestExcepciones(unittest.TestCase):

    def test_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoExcepcion):
            raise PacienteNoEncontradoExcepcion("No se ha encontrado al paciente.")

    def test_medico_no_encontrado(self):
        with self.assertRaises(MedicoNoEncontrado):
            raise MedicoNoEncontrado("No se ha encontrado al medico.")

    def test_medico_no_disponible(self):
        with self.assertRaises(MedicoNoDisponibleExcepcion):
            raise MedicoNoDisponibleExcepcion("Medico no disponible")

    def test_turno_ocupado(self):
        with self.assertRaises(TurnoOcupadoException):
            raise TurnoOcupadoException("El turno solicitado ya se encuentra ocupado.")

    def test_receta_invalida(self):
        with self.assertRaises(RecetaInvalidaException):
            raise RecetaInvalidaException("Receta inválida")

    def test_error_al_agregar_paciente(self):
        with self.assertRaises(ErrorAlAgregarPaciente):
            raise ErrorAlAgregarPaciente("Ocurrio un error al agregar al paciente.")

    def test_error_al_agregar_medico(self):
        with self.assertRaises(ErrorAlAgregarMedico):
            raise ErrorAlAgregarMedico("Ocurrio un error al agregar el medico.")

    def test_especialidad_ya_existente(self):
        with self.assertRaises(EspecialidadYaExistente):
            raise EspecialidadYaExistente("Esta especialidad ya le corresponde al medico.")

if __name__ == "__main__":
    unittest.main()
