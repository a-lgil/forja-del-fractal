import math
import time
import streamlit as st

import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex

# icon snowflake
st.set_page_config(page_title='SFI Fractal', layout='wide', page_icon='❄')

def sistema_funciones_iteradas(sfi, pasos, semilla):
    '''
    Función que implementa el algoritmo determinista para la obtención del fractal asociado a un sistema
    de funciones iteradas (SFI)
    '''
    # Inicializamos el punto inicial con la semilla
    punto_inicial = semilla

    # Inicializamos la lista de puntos con el punto inicial
    lista_puntos = [punto_inicial]

    # Inicializamos la nueva lista de puntos vacía
    nueva_lista_puntos = []

    # Inicializamos las listas de puntos para cada función en SFI
    puntos_por_funcion = [[] for _ in range(len(sfi))]

    # Iteramos el número de veces especificado
    for i in range(pasos):
        # Iteramos sobre cada punto de la lista de puntos
        for j in range(len(lista_puntos)):
            # Iteramos sobre cada función del sistema de funciones iteradas
            for k in range(len(sfi)):
                # Obtenemos el punto original
                x = lista_puntos[j][0]
                y = lista_puntos[j][1]

                # Obtenemos los coeficientes de la función k
                a = sfi[k][0]
                b = sfi[k][1]
                c = sfi[k][2]
                d = sfi[k][3]
                e = sfi[k][4]
                f = sfi[k][5]

                # Calculamos el punto resultante
                punto_resultante = (a * x + b * y + e, c * x + d * y + f)

                # Añadimos el punto resultante a la lista de puntos correspondiente
                puntos_por_funcion[k].append(punto_resultante)

                # Añadimos el punto resultante a la nueva lista de puntos
                nueva_lista_puntos.append(punto_resultante)

        # Actualizamos la lista de puntos
        lista_puntos = nueva_lista_puntos

        # Vaciamos la nueva lista de puntos
        nueva_lista_puntos = []

    # Devolvemos las listas de puntos para cada función en SFI
    return puntos_por_funcion

# Dibujamos los puntos
def dibujar_fractal(puntos_por_funcion, colormap, point_size):

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 15)
    ax.axis('equal')

    # # limit axis to max and min values
    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)

    # Create a colormap

    for i, puntos in enumerate(puntos_por_funcion):
        x = [p[0] for p in puntos]
        y = [p[1] for p in puntos]
        color = colormap[i % len(colormap)]

        ax.scatter(x, y, s=point_size, c=color)

    return fig

# DATABASE OF IFS -------------------------------------------------------------
sierpinski_triangulo = [[0.5,       0,      0,      0.5,    0,      0,      0.333],
                        [0.5,       0,      0,      0.5,    0.5,    0,      0.333],
                        [0.5,       0,      0,      0.5,    0.25,   0.433,  0.334]]

sierpinski_alfombra = [[0.333, 0.0, 0.0, 0.333, 0.0, 0.0],
                       [0.333, 0.0, 0.0, 0.333, 0.333, 0.0],
                       [0.333, 0.0, 0.0, 0.333, 0.667, 0.0],
                       [0.333, 0.0, 0.0, 0.333, 0.0, 0.333],
                       [0.333, 0.0, 0.0, 0.333, 0.667, 0.333],
                       [0.333, 0.0, 0.0, 0.333, 0.0, 0.667],
                       [0.333, 0.0, 0.0, 0.333, 0.333, 0.667],
                       [0.333, 0.0, 0.0, 0.333, 0.667, 0.667]]

squares = [[0.45,      0,      0,      0.45,   0,      0,      0.35],
           [0.4,       0,      0,      0.4,    0.6,    0,      0.28],
           [0.35,      0,      0,      0.35,   0,      0.65,   0.21],
           [0.3,       0,      0,      0.3,    0.7,    0.7,    0.16]]

koch = [[0.333,     0,      0,      0.333,  0,      0,      0.25],
        [0.166,     -0.288, 0.288,  0.166,  0.333,  0,      0.25],
        [0.166,     0.288,  -0.288, 0.166,  0.5,    0.288,  0.25],
        [0.333,     0,      0,      0.333,  0.666,  0,      0.25]]

koch_copo = [[0.5, 0.289, -0.289, 0.5, 0.0, 0.0],
             [0.333, 0.0, 0.0, 0.333, 0.577, 0.333],
             [0.333, 0.0, 0.0, 0.333, 0.0, 0.667],
             [0.333, 0.0, 0.0, 0.333, -0.577, 0.333],
             [0.333, 0.0, 0.0, 0.333, -0.577, -0.333],
             [0.333, 0.0, 0.0, 0.333, 0.0, -0.667],
             [0.333, 0.0, 0.0, 0.333, 0.577, -0.333]]

barnsley = [[0.849,     0.037,  -0.037, 0.849,  0.075,  0.183,  0.85],
            [0.197,     -0.226, 0.225,  0.197,  0.4,    0.049,  0.07],
            [-0.15,     0.283,  0.25,   0.237,  0.575,  -0.084, 0.07],
            [0,         0,      0,      0.16,   0.5,    0,      0.01]]

cantor = [[0.333,       0,      0,      0,    0,      0],
          [0.333,       0,      0,      0,    2,      0]]

cantor_2 = [[0.2,       0,      0,      0,    0,      0],
            [0.2,       0,      0,      0,    2,      0],
            [0.2,       0,      0,      0,    4,      0]]
        
problema_aleatorio_ifs_1 = [[1/2,       0,      0,      1/2,    0,      1/2],
                            [0,         1/2,    -1/2,   0,      1/2,    1/2],
                            [1/2,       0,      0,      -1/2,   0,      1/2]]

problema_aleatorio_ifs_2 = [[1/3,       0,      0,      1/3,    0,      0],
                            [1/3,       0,      0,      1/3,    0,      2/3],
                            [1/3,       0,      0,      1/3,    1/3,    1/3],
                            [1/3,       0,      0,      1/3,    2/3,    0],
                            [1/3,       0,      0,      1/3,    2/3,    2/3]]

problema_aleatorio_ifs_3 = [[1/2,       0,      0,      1/2,    0,      0],
                            [-1/2,      0,      0,      -1/2,   1/2,    1],
                            [-1/2,      0,      0,      -1/2,   1,      1/2]]

problema_aleatorio_ifs_4 = [[1/2,       0,      0,      1/2,    0,      0],
                            [0,         -1/2,   1/2,    0,      1/2,    1/2],
                            [0,         -1/2,   1/2,    0,      1,      0]]

problema_aleatorio_ifs_5 = [[1/3,       0,      0,      1/3,    0,      0],
                            [1/3,       0,      0,      1/3,    1/3,    0],
                            [1/3,       0,      0,      1/3,    0,      1/3],
                            [1/3,       0,      0,      1/3,    2/3,    0],
                            [1/3,       0,      0,      1/3,    0,      2/3]]

problema_aleatorio_ifs_6 = [[1/2,       0,      0,      1/2,    0,      0],
                            [1/2,       0,      0,      1/2,    0,      1/2],
                            [0,         -1/2,   -1/2,   0,      1,      1/2]]

problema_aleatorio_ifs_7 = [[1/2,       0,      0,      1/2,    0,      0],
                            [-1/2,      0,      0,      1/2,    1,      0],
                            [0,         1/2,    -1/2,   0,      0,      1]]

atractor_ifs_6 = [  [0.255,     0,      0,      0.255,  0.3726, 0.6714],
                    [0.255,     0,      0,      0.255,  0.1146, 0.2232],
                    [0.255,     0,      0,      0.255,  0.6306, 0.2232],
                    [0.37,      -0.642, 0.642,  0.37,   0.6356,-0.0061]]

copo_de_nieve_raruno = [[0.333, 0.0, 0.0, 0.333, 0.577, 0.333],
                        [0.333, 0.0, 0.0, 0.333, 0.0, 0.667],
                        [0.333, 0.0, 0.0, 0.333, -0.577, 0.333],
                        [0.333, 0.0, 0.0, 0.333, -0.577, -0.333],
                        [0.333, 0.0, 0.0, 0.333, 0.0, -0.667],
                        [0.333, 0.0, 0.0, 0.333, 0.577, -0.333],
                        [0.0, 0.0, 0.0, 1.1, 0.0, 0.0],
                        [0.0, -0.952, 0.0, 0.55, 0.0, 0.0],
                        [0.0, 0.952, 0.0, 0.55, 0.0, 0.0],
                        [0.577, -0.334, 0.334, 0.577, 0.0, 0.0],
                        [0.2, 0.0, 0.0, 0.2, 0.0, 0.0],
                        [0.26, 0.15, -0.15, 0.26, 0.0, 0.0]]

# empty IFS with 15 rows and 6 columns all filled with 0s
ifs_vacio = [[0 for i in range(6)] for j in range(15)]

# STREAMLIT APP ---------------------------------------------------------------

# save use_ifs in session state
if 'use_ifs' not in st.session_state:
    st.session_state.use_ifs = False

settings_col, viewer_col = st.columns(2)

# Settings
with settings_col:

    st.title('Generador de fractales con SFI')

    st.subheader('Parámetros')

    # Use pre-defined IFS
    use_ifs = st.checkbox('Usar IFS predefinido', value=True)

    if use_ifs:

        # selectbox to choose the IFS
        ifs = st.selectbox('IFS', ('Triángulo de Sierpinski', 'Alfombra de Sierpinski', 'Curva de Koch', 'Copo de Koch', 
                                   'Helecho de Barnsley', 'Cuadradetes', 'Cantor', 'Cantor Final 2020 Ej 2', 'Copo de nieve raruno',
                                'Problema aleatorio 1', 'Problema aleatorio 2', 'Problema aleatorio 3', 'Problema aleatorio 4',
                                'Problema aleatorio 5', 'Problema aleatorio 6', 'Problema aleatorio 7', 'Atractor 6'), label_visibility='collapsed', index=0)

        ifs_dict = {'Triángulo de Sierpinski': sierpinski_triangulo, 'Alfombra de Sierpinski': sierpinski_alfombra,
                    'Curva de Koch': koch, 'Copo de Koch': koch_copo, 'Helecho de Barnsley': barnsley,
                    'Cuadradetes': squares, 'Cantor': cantor, 'Cantor Final 2020 Ej 2': cantor_2, 'Copo de nieve raruno': copo_de_nieve_raruno,

                    'Problema aleatorio 1': problema_aleatorio_ifs_1, 'Problema aleatorio 2': problema_aleatorio_ifs_2,
                    'Problema aleatorio 3': problema_aleatorio_ifs_3, 'Problema aleatorio 4': problema_aleatorio_ifs_4,
                    'Problema aleatorio 5': problema_aleatorio_ifs_5, 'Problema aleatorio 6': problema_aleatorio_ifs_6,
                    'Problema aleatorio 7': problema_aleatorio_ifs_7,
                    
                    'Atractor 6': atractor_ifs_6
                    }
        
        ifs = ifs_dict[ifs] # type: ignore

    else:
        ifs = ifs_vacio

    # Setttings columns
    settings_col_1, settings_col_2, settings_col_3, settings_col_4, settings_col_5 = st.columns(5)

    # Number of rows in the IFS
    with settings_col_1:
        num_rows = st.number_input('Columnas', min_value=1, max_value=15, value=3 if not use_ifs else len(ifs), step=1)

    # pasos = 50000
    # semilla = (0, 0)
    with settings_col_2:

        max_pasos = int(math.log(3000000, num_rows))

        pasos = st.number_input('Pasos', min_value=1, max_value=min(max_pasos, 7), value=max_pasos-1, step=1)

    with settings_col_3:
        semilla_x = st.number_input('Semilla x', min_value=-10.0, max_value=10.0, value=0.0, step=0.01)

    with settings_col_4:
        semilla_y = st.number_input('Semilla y', min_value=-10.0, max_value=10.0, value=0.0, step=0.01)

    semilla = (semilla_x, semilla_y)

    with settings_col_5:
        point_size = st.number_input('Tamaño puntos', min_value=0.001, max_value=100.0, value=0.05, step=1.0)

    # divider
    st.subheader('IFS')

    # Create 6 columns in the streamlit app (a, b, c, d, e, f)
    def create_columns(i):
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        if i == 0:
            col1.write('a')
            col2.write('b')
            col3.write('c')
            col4.write('d')
            col5.write('e')
            col6.write('f')
            col7.write('color')

        return col1, col2, col3, col4, col5, col6, col7

    colormap = plt.get_cmap('tab10')

    # For each row, create manual text input for numbers
    a, b, c, d, e, f, color = [], [], [], [], [], [], []

    if use_ifs:
        for i in range(num_rows): # type: ignore
            col1, col2, col3, col4, col5, col6, col7 = create_columns(i)
            # in case the ifs has less rows than num_rows, fill the rest with 0s
            if i >= len(ifs):
                ifs.append([0, 0, 0, 0, 0, 0])
            a.append(col1.text_input(f'a{i}', value=ifs[i][0], label_visibility='collapsed'))
            b.append(col2.text_input(f'b{i}', value=ifs[i][1], label_visibility='collapsed'))
            c.append(col3.text_input(f'c{i}', value=ifs[i][2], label_visibility='collapsed'))
            d.append(col4.text_input(f'd{i}', value=ifs[i][3], label_visibility='collapsed'))
            e.append(col5.text_input(f'e{i}', value=ifs[i][4], label_visibility='collapsed'))
            f.append(col6.text_input(f'f{i}', value=ifs[i][5], label_visibility='collapsed'))
            rgba = colormap(i % colormap.N)
            hex_color = rgb2hex(rgba[:3])
            with col7:
                color.append(st.color_picker(f'color{i}', value=hex_color, label_visibility='collapsed'))
                # add space between rows
    else:
        for i in range(num_rows):
            col1, col2, col3, col4, col5, col6, col7 = create_columns(i)
            a.append(col1.text_input(f'a{i}', value=0, label_visibility='collapsed'))
            b.append(col2.text_input(f'b{i}', value=0, label_visibility='collapsed'))
            c.append(col3.text_input(f'c{i}', value=0, label_visibility='collapsed'))
            d.append(col4.text_input(f'd{i}', value=0, label_visibility='collapsed'))
            e.append(col5.text_input(f'e{i}', value=0, label_visibility='collapsed'))
            f.append(col6.text_input(f'f{i}', value=0, label_visibility='collapsed'))
            rgba = colormap(i % colormap.N)
            hex_color = rgb2hex(rgba[:3])
            color.append(col7.color_picker(f'color{i}', value=hex_color, label_visibility='collapsed'))

    col1, col2 = st.columns([1, 3])

    with col2:
        update = st.checkbox('Actualizar automáticamente', value=True)

    with col1:
        generate_fractal = st.button('Generar fractal', disabled=update, use_container_width=True)

with viewer_col:

    # Now we have to save this a, b, c, d, e, f in a list of lists to generate the IFS
    ifs = []

    for i in range(num_rows): # type: ignore
        ifs.append([float(a[i]) if a[i] != '' else 0,
                    float(b[i]) if b[i] != '' else 0,
                    float(c[i]) if c[i] != '' else 0,
                    float(d[i]) if d[i] != '' else 0,
                    float(e[i]) if e[i] != '' else 0,
                    float(f[i]) if f[i] != '' else 0,
                ])

    # # Plot settings, points and lines on and off and sizes
    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     show_points = st.checkbox('Puntos', value=True)
        
    # with col2:
    #     show_lines = st.checkbox('Líneas', value=False)

    # with col1:
    #     if show_points:
    #         
    
    # if show_lines:
    #     with col2:
    #         line_width = st.number_input('Ancho líneas', min_value=0.001, max_value=100.0, value=0.5, step=1.0)
    #         with col3:
    #             interpolate = st.checkbox('Interpolar', value=False)

    # Now we have to plot the IFS
    if generate_fractal or update:

        start_time = time.time()

        puntos_fractal = sistema_funciones_iteradas(ifs, pasos, semilla)

        # Generando fractal...
        st.spinner('Generando fractal...')

        fractal = dibujar_fractal(puntos_fractal, color, point_size)

        end_time = time.time()

        st.pyplot(fractal)

        st.caption(f'Fractal con {sum([len(p) for p in puntos_fractal])} puntos generado en {round(end_time-start_time, 3)} segundos')

        st.write('Código IFS:')
        st.text(ifs)