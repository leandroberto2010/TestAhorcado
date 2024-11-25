import pyautogui as pag
import subprocess as sp
import pytest
import time


@pytest.fixture(scope="function")

def iniciar_aplicacion():
    """Inicia la aplicación antes de cada prueba y la cierra después."""
    print("iniciando")
    process = sp.Popen(['python', 'AhorcadoApp.py'])
    time.sleep(3)  # Espera para que la aplicación se inicie completamente
    yield process
    process.terminate()
    process.wait()
    time.sleep(2)

def test_ganar_letra(iniciar_aplicacion):
    textInput = pag.locateOnScreen('textInput.png')
    pag.click(pag.center(textInput))
    pag.write("PALABRA")

    startButton = pag.locateOnScreen('empezar_juego.png')
    pag.click(pag.center(startButton))

    letraInput = pag.locateOnScreen("letra_input.png")
    
    letraButton = pag.locateOnScreen("adivinar_letra.png")

    for letra in "PALBR":
        pag.click(pag.center(letraInput))
        pag.write(letra)
        pag.click(pag.center(letraButton))

    ganasteMsg = pag.locateOnScreen("ganaste.png")
    
    assert ganasteMsg is not pag.ImageNotFoundException

def test_adivinar_palabra(iniciar_aplicacion):
    textInput = pag.locateOnScreen("textInput.png")
    pag.click(pag.center(textInput))
    pag.write("PALABRA")

    startButton = pag.locateOnScreen('empezar_juego.png')
    pag.click(pag.center(startButton))

    palabraInput = pag.locateOnScreen("palabra_input.png")
    pag.click(pag.center(palabraInput))
    pag.write("PALABRA")

    adivinarPalabraButton = pag.locateOnScreen("adivinar_palabra.png")
    pag.click(pag.center(adivinarPalabraButton))

    ganasteMsg = pag.locateOnScreen("ganaste.png")

    assert ganasteMsg is not None