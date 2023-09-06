from prettytable import PrettyTable

class Paciente:
    def __init__(self, documento, nombre, sexo, fecha_nacimiento):
        self.documento = documento
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.signos_vitales = {}
        self.notas_medicas = ""
        self.imagenes_diagnosticas = []
        self.resultados_laboratorio = []
        self.medicamentos = []

    def agregar_signos_vitales(self, signos_vitales):
        self.signos_vitales = signos_vitales

    def agregar_notas_medicas(self, notas_medicas):
        self.notas_medicas = notas_medicas

    def agregar_imagenes_diagnosticas(self, imagenes_diagnosticas):
        self.imagenes_diagnosticas.append(imagenes_diagnosticas)

    def agregar_resultados_laboratorio(self, resultados_laboratorio):
        self.resultados_laboratorio.append(resultados_laboratorio)

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)


class HistoriaClinica:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def obtener_paciente_por_documento(self, documento):
        for paciente in self.pacientes:
            if paciente.documento == documento:
                return paciente

        return None


class GeneradorReportes:
    def __init__(self, historia_clinica):
        self.historia_clinica = historia_clinica

    def generar_porcentaje_ocupacion(self):
        total_camas = 300
        camas_ocupadas = len(self.historia_clinica.pacientes)
        porcentaje_ocupacion = camas_ocupadas / total_camas * 100
        print(f"Porcentaje de ocupación: {porcentaje_ocupacion}%")

    def generar_estancia_promedio_por_servicio(self):
        pass

    def generar_admisiones_y_altas_por_servicio(self):
        pass

    def generar_pacientes_con_enfermedades_cronicas(self):
        pass

    def generar_medicamentos_prescritos_por_servicio(self):
        pass



historia_clinica = HistoriaClinica()

cantidad_pacientes = input("¿Cuántos pacientes desea registrar? ")

for i in range(int(cantidad_pacientes)):
    print("Ingrese los datos del ",i+1 ," paciente:")
    documento = input("Documento: ")
    nombre = input("Nombre: ")
    sexo = input("Sexo: ")
    fecha_nacimiento = input("Fecha de nacimiento (formato: dd/mm/aaaa): ")
    paciente = Paciente(documento, nombre, sexo, fecha_nacimiento)

    signos_vitales = {}
    signos_vitales["presion_arterial"] = input("Presión arterial: ")
    signos_vitales["temperatura"] = input("Temperatura: ")
    signos_vitales["saturacion_O2"] = input("Saturación de oxígeno: ")
    signos_vitales["frecuencia_respiratoria"] = input("Frecuencia respiratoria: ")
    paciente.agregar_signos_vitales(signos_vitales)

    notas_medicas = input("Notas médicas: ")
    paciente.agregar_notas_medicas(notas_medicas)

    historia_clinica.agregar_paciente(paciente)


generador_reportes = GeneradorReportes(historia_clinica)
generador_reportes.generar_porcentaje_ocupacion()


tabla_pacientes = PrettyTable()
tabla_pacientes.field_names = ["Documento", "Nombre", "Sexo", "Fecha de nacimiento", "Presión arterial", "Temperatura", "Saturación de oxígeno", "Frecuencia respiratoria", "Notas médicas"]

for paciente in historia_clinica.pacientes:
    tabla_pacientes.add_row([paciente.documento, paciente.nombre, paciente.sexo, paciente.fecha_nacimiento, paciente.signos_vitales["presion_arterial"], paciente.signos_vitales["temperatura"], paciente.signos_vitales["saturacion_O2"], paciente.signos_vitales["frecuencia_respiratoria"], paciente.notas_medicas])

print(tabla_pacientes)
