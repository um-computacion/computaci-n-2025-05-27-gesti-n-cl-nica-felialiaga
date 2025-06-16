class PacienteNoEncontradoExcepcion(Exception):
    print('No se ha encontrado al paciente.')

class MedicoNoEncontrado(Exception):
    print("No se ha encontrado al medico.")

class MedicoNoDisponibleExcepcion(Exception):
    print("El medico no se encuentra disponible ese dia")

class TurnoOcupadoException(Exception):
    print('El turno solicitado ya se encuentra ocupado.')

class RecetaInvalidaException(Exception):
    pass

class ErrorAlAgregarPaciente(Exception):
    print("Ocurrio un error al agregar al paciente.")

class ErrorAlAgregarMedico(Exception):
    print("Ocurrio un error al agregar el medico.")

class EspecialidadYaExistente(Exception):
    print("Esta especialidad ya le corresponde al medico.")

class ErrorGeneralTurno(Exception):
    pass

class ErrorGeneralClinica(Exception):
    pass

class ErrorPaciente(Exception):
    pass

class ErrorMedico(Exception):
    pass