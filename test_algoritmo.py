# Algoritmo básico de clasificación de prioridad (Simulación Norma MINSA)
def clasificar_prioridad(frecuencia_cardiaca, temperatura):
    # Si tiene taquicardia severa o fiebre extrema es Prioridad 1 (Emergencia)
    if frecuencia_cardiaca > 120 or temperatura >= 39.5:
        return "Prioridad 1"
    return "Prioridad 3"

# La prueba unitaria automatizada que ejecutará GitHub Actions
def test_clasificacion_emergencia():
    # Simulamos un paciente crítico
    resultado = clasificar_prioridad(frecuencia_cardiaca=130, temperatura=39.8)
    
    # Validamos que el algoritmo responda correctamente
    assert resultado == "Prioridad 1"