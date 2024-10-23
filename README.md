# 🎮 PyWordle Español

Un clon del popular juego Wordle implementado en Python, con interfaz gráfica y versión de consola. ¡Adivina la palabra en 6 intentos!

## 📝 Descripción

PyWordle es una implementación en Python del famoso juego de palabras Wordle, adaptado al español. El juego incluye dos versiones:
- 🖥️ Versión con interfaz gráfica (GUI) usando Tkinter
- ⌨️ Versión de consola con emojis

### Características

- 🎯 6 intentos para adivinar la palabra
- 🔤 Palabras de 5 letras en español
- 🎨 Retroalimentación visual con colores
- ⌨️ Control mediante teclado
- 💾 Fácil de ejecutar y modificar

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/pywordle-esp.git
cd pywordle-esp
```

2. Asegúrate de tener Python 3.6 o superior instalado:
```bash
python --version
```

3. No se requieren dependencias adicionales, ¡el juego usa solo la biblioteca estándar de Python!

## 🎮 Uso

### Versión GUI:
```bash
python wordle_gui.py
```

### Versión Consola:
```bash
python wordle_console.py
```

### Cómo Jugar

1. El objetivo es adivinar la palabra de 5 letras
2. Después de cada intento, el juego te dará pistas:
   - 🟩 Verde: Letra correcta en posición correcta
   - 🟨 Amarillo: Letra correcta en posición incorrecta
   - ⬜ Gris: Letra no está en la palabra
3. Tienes 6 intentos para adivinar la palabra

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- Tkinter (para la versión GUI)
- Biblioteca estándar de Python

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. Haz Fork del proyecto
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Haz Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📝 TODO

- [ ] Agregar más palabras al diccionario
- [ ] Implementar sistema de puntuación
- [ ] Agregar estadísticas de juego
- [ ] Crear teclado virtual en pantalla
- [ ] Añadir animaciones
- [ ] Implementar sistema de guardado de progreso

## 🌟 Agradecimientos

- Inspirado en el juego original [Wordle](https://www.nytimes.com/games/wordle/index.html)
- Gracias a todos los contribuidores y jugadores
