import streamlit as st
import pandas as pd
import random
import json
import os
from datetime import datetime, timedelta, date
import plotly.express as px

from data.menu_generator import MenuGenerator
from data.inventory import InventoryManager
from utils.nutrition import NutritionCalculator
from utils.precios_dane import PreciosActualizados

st.set_page_config(
    page_title="Planificador de Comidas | Julian y Annmar",
    page_icon="🥗",
    layout="wide"
)

PERSONA1 = "Julian"
PERSONA2 = "Annmar"
PESO1 = 85
PESO2 = 56
DIAS_PLAN = 15
FECHA_INICIO = date(2026, 6, 3)   # Cambia aquí cuando empieces un plan nuevo
ARCHIVO_MENU = "data/menu_guardado.json"

calc = NutritionCalculator(PERSONA1, PESO1, PERSONA2, PESO2)
metas = calc.get_metas_personalizadas()

# ---------- FUNCION PARA MENU FIJO ----------
def cargar_o_generar_menu():
    """Carga el menú desde JSON si existe y la fecha coincide, si no, genera uno nuevo con semilla fija."""
    if os.path.exists(ARCHIVO_MENU):
        with open(ARCHIVO_MENU, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data.get('fecha_inicio') == str(FECHA_INICIO):
            return data['menu']
    # Generar nuevo
    random.seed(str(FECHA_INICIO))
    mg = MenuGenerator(dias=DIAS_PLAN, personas=2)
    menu = mg.generar_menu()
    os.makedirs('data', exist_ok=True)
    with open(ARCHIVO_MENU, 'w', encoding='utf-8') as f:
        json.dump({'fecha_inicio': str(FECHA_INICIO), 'menu': menu}, f, indent=2, ensure_ascii=False)
    return menu

# ---------- INICIALIZAR SESION ----------
if 'menu' not in st.session_state:
    st.session_state.menu = cargar_o_generar_menu()
    st.session_state.menu_generator = MenuGenerator(dias=DIAS_PLAN, personas=2)
    st.session_state.menu_generator.menu = st.session_state.menu
    st.session_state.inventory_manager = InventoryManager(st.session_state.menu)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("🥗 Plan Nutricional")
    st.markdown("---")
    st.markdown(f"### 👤 {PERSONA1}")
    st.write(f"Peso: {PESO1} kg")
    st.write(f"Meta: {metas['persona1']['calorias_mantencion']} kcal/dia")
    st.markdown(f"### 👤 {PERSONA2}")
    st.write(f"Peso: {PESO2} kg")
    st.write(f"Meta: {metas['persona2']['calorias_mantencion']} kcal/dia")
    st.markdown("---")
    st.markdown("### 🎯 Objetivo")
    st.write("Mantener peso actual")
    st.write("Comida colombo-venezolana")

st.title("🥗 Planificador de Comidas Saludable")
st.markdown(f"### ¡Bienvenidos {PERSONA1} y {PERSONA2}!")
st.markdown("---")

# ---------- PESTAÑAS ----------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📅 Menu Diario",
    "📋 Inventario y Compras",
    "📊 Analisis Nutricional",
    "📖 Recetario",
    "🧊 Congelar y Porcionar"
])

# ========== TAB 1: MENU DIARIO ==========
with tab1:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.header("📅 Plan de Comidas")
    with col2:
        if st.button("🔄 Regenerar Menu", use_container_width=True):
            if os.path.exists(ARCHIVO_MENU):
                os.remove(ARCHIVO_MENU)
            st.session_state.menu = cargar_o_generar_menu()
            st.session_state.menu_generator.menu = st.session_state.menu
            st.session_state.inventory_manager = InventoryManager(st.session_state.menu)
            st.rerun()

    dia_seleccionado = st.selectbox(
        "Seleccionar dia:",
        range(1, DIAS_PLAN + 1),
        format_func=lambda x: f"Dia {x} - {(datetime.now() + timedelta(days=x-1)).strftime('%d/%m/%Y')}"
    )

    dia_menu = st.session_state.menu[dia_seleccionado - 1]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🌅 Desayuno")
        with st.expander(f"{dia_menu['desayuno']['nombre']}", expanded=True):
            st.caption(f"{dia_menu['desayuno']['tiempo_preparacion']} | {dia_menu['desayuno']['dificultad']}")
            st.write("**Ingredientes:**")
            for ing, datos in dia_menu['desayuno']['ingredientes'].items():
                st.write(f"- {ing.replace('_', ' ').title()}: {datos['cantidad']} {datos['unidad']}")
            nutri = dia_menu['desayuno']['informacion_nutricional']
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Calorias", f"{nutri['calorias']} kcal")
                st.metric("Proteinas", f"{nutri['proteinas']}g")
            with col_b:
                st.metric("Carbohidratos", f"{nutri['carbohidratos']}g")
                st.metric("Grasas", f"{nutri['grasas']}g")
            st.write("**Preparacion:**")
            for i, paso in enumerate(dia_menu['desayuno']['preparacion'], 1):
                st.write(f"{i}. {paso}")

    with col2:
        st.subheader("☀️ Almuerzo")
        with st.expander(f"{dia_menu['almuerzo']['nombre']}", expanded=True):
            st.caption(f"{dia_menu['almuerzo']['tiempo_preparacion']} | {dia_menu['almuerzo']['dificultad']}")
            st.write("**Ingredientes:**")
            for ing, datos in dia_menu['almuerzo']['ingredientes'].items():
                st.write(f"- {ing.replace('_', ' ').title()}: {datos['cantidad']} {datos['unidad']}")
            nutri = dia_menu['almuerzo']['informacion_nutricional']
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Calorias", f"{nutri['calorias']} kcal")
                st.metric("Proteinas", f"{nutri['proteinas']}g")
            with col_b:
                st.metric("Carbohidratos", f"{nutri['carbohidratos']}g")
                st.metric("Grasas", f"{nutri['grasas']}g")
            st.write("**Preparacion:**")
            for i, paso in enumerate(dia_menu['almuerzo']['preparacion'], 1):
                st.write(f"{i}. {paso}")

    with col3:
        st.subheader("🌙 Cena")
        with st.expander(f"{dia_menu['cena']['nombre']}", expanded=True):
            st.caption(f"{dia_menu['cena']['tiempo_preparacion']} | {dia_menu['cena']['dificultad']}")
            st.write("**Ingredientes:**")
            for ing, datos in dia_menu['cena']['ingredientes'].items():
                st.write(f"- {ing.replace('_', ' ').title()}: {datos['cantidad']} {datos['unidad']}")
            nutri = dia_menu['cena']['informacion_nutricional']
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Calorias", f"{nutri['calorias']} kcal")
                st.metric("Proteinas", f"{nutri['proteinas']}g")
            with col_b:
                st.metric("Carbohidratos", f"{nutri['carbohidratos']}g")
                st.metric("Grasas", f"{nutri['grasas']}g")
            st.write("**Preparacion:**")
            for i, paso in enumerate(dia_menu['cena']['preparacion'], 1):
                st.write(f"{i}. {paso}")

    st.markdown("---")
    resumen = dia_menu['resumen_nutricional']
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Calorias Totales", f"{resumen['calorias_totales']} kcal")
    with col2:
        st.metric("Proteinas Totales", f"{resumen['proteinas_totales']}g")
    with col3:
        st.metric("Carbohidratos", f"{resumen['carbohidratos_totales']}g")
    with col4:
        porcentaje = (resumen['calorias_totales'] / metas['persona1']['calorias_mantencion']) * 100
        st.metric(f"% Meta {PERSONA1}", f"{porcentaje:.0f}%")

# ========== TAB 2: INVENTARIO ==========
with tab2:
    st.header("📋 Gestion de Inventario y Lista de Mercado")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📦 Mi Inventario Actual")
        with st.form("inventario_form"):
            st.write("Ingresa lo que tienes en casa:")
            inventario_actual = {}
            for categoria, productos in st.session_state.inventory_manager.categorias_productos.items():
                productos_necesarios = [p for p in productos if p in st.session_state.inventory_manager.inventario_necesario]
                if productos_necesarios:
                    st.write(f"**{categoria}**")
                    for producto in productos_necesarios:
                        datos = st.session_state.inventory_manager.inventario_necesario[producto]
                        col_a, col_b = st.columns([3, 1])
                        with col_a:
                            st.caption(f"{producto.replace('_', ' ').title()} (Necesario: {datos['cantidad']} {datos['unidad']})")
                        with col_b:
                            inventario_actual[producto] = st.number_input(
                                "Tengo", min_value=0.0, value=0.0, step=0.1,
                                key=f"inv_{producto}", label_visibility="collapsed"
                            )
            if st.form_submit_button("💾 Guardar Inventario", use_container_width=True):
                st.session_state.inventory_manager.actualizar_inventario_actual(inventario_actual)
                st.success("Inventario guardado!")
                st.rerun()

    with col2:
        st.subheader("🛒 Lista de Mercado")
        ciudad = st.selectbox("📍 Tu ciudad:", ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira"])
        if st.session_state.inventory_manager.inventario_actual:
            lista_compras = st.session_state.inventory_manager.generar_lista_compras()
            compras_organizadas = st.session_state.inventory_manager.organizar_por_categorias(lista_compras)
            if compras_organizadas:
                st.warning("📋 Productos a comprar:")
                for categoria, productos in compras_organizadas.items():
                    with st.expander(f"{categoria} ({len(productos)} productos)"):
                        for producto, datos in productos.items():
                            st.write(f"- {producto.replace('_', ' ').title()}: {datos['cantidad']} {datos['unidad']}")
                st.markdown("---")
                st.subheader("💰 Presupuesto Estimado")
                gestor_precios = PreciosActualizados()
                gestor_precios.ajustar_precios_por_ciudad(ciudad)
                resultado = gestor_precios.calcular_costo_lista(lista_compras)
                st.metric(label="💰 Costo Total Estimado", value=f"${resultado['total']:,.0f} COP", delta=f"Precios {ciudad}")
                with st.expander("📊 Ver desglose por producto"):
                    for categoria, productos in compras_organizadas.items():
                        st.write(f"**{categoria}**")
                        total_categoria = 0
                        for producto in productos:
                            if producto in resultado['desglose']:
                                detalle = resultado['desglose'][producto]
                                precio = detalle['costo']
                                total_categoria += precio
                                st.write(f"- {producto.replace('_', ' ').title()}: ${precio:,.0f}")
                        st.write(f"*Subtotal: ${total_categoria:,.0f}*")
                        st.write("---")
            else:
                st.success("Tienes todo lo necesario!")
        else:
            st.info("👈 Guarda tu inventario para generar la lista de compras")

# ========== TAB 3: ANALISIS NUTRICIONAL ==========
with tab3:
    st.header("📊 Analisis Nutricional")
    analisis = calc.analizar_menu(st.session_state.menu)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Promedio Calorias/Dia", f"{analisis['promedio_calorias']} kcal")
    with col2:
        st.metric("Promedio Proteinas/Dia", f"{analisis['promedio_proteinas']}g")
    with col3:
        st.metric("Dias planificados", DIAS_PLAN)

    st.subheader("📈 Evolucion de Calorias por Dia")
    calorias_por_dia = [dia['resumen_nutricional']['calorias_totales'] for dia in st.session_state.menu]
    df = pd.DataFrame({
        "Dia": range(1, DIAS_PLAN + 1),
        "Calorias": calorias_por_dia,
        f"Meta {PERSONA1}": [metas['persona1']['calorias_mantencion']] * DIAS_PLAN,
        f"Meta {PERSONA2}": [metas['persona2']['calorias_mantencion']] * DIAS_PLAN
    })
    fig = px.line(df, x="Dia", y=["Calorias", f"Meta {PERSONA1}", f"Meta {PERSONA2}"], title="Calorias por Dia vs Metas")
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        prom_desayuno = sum(d['desayuno']['informacion_nutricional']['calorias'] for d in st.session_state.menu) / DIAS_PLAN
        prom_almuerzo = sum(d['almuerzo']['informacion_nutricional']['calorias'] for d in st.session_state.menu) / DIAS_PLAN
        prom_cena = sum(d['cena']['informacion_nutricional']['calorias'] for d in st.session_state.menu) / DIAS_PLAN
        df_comidas = pd.DataFrame({"Comida": ["Desayuno", "Almuerzo", "Cena"], "Calorias": [prom_desayuno, prom_almuerzo, prom_cena]})
        fig2 = px.pie(df_comidas, values="Calorias", names="Comida", title="Distribucion Calorica")
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.subheader("💡 Recomendaciones")
        for rec in analisis['recomendaciones']:
            st.write(rec)
        st.info(f"""
        **{PERSONA1}** (85 kg): {metas['persona1']['calorias_mantencion']} kcal/dia
        **{PERSONA2}** (56 kg): {metas['persona2']['calorias_mantencion']} kcal/dia
        - Beber 2-3 litros de agua al dia
        - Realizar 30 min de actividad fisica
        - Evitar azucares refinados
        """)

# ========== TAB 4: RECETARIO ==========
with tab4:
    st.header("📖 Recetario Completo")
    categoria_recetas = st.selectbox("Filtrar por categoria:", ["Todas", "Desayunos", "Almuerzos", "Cenas"])
    recetas_mostrar = st.session_state.menu_generator.get_todas_las_recetas()
    if categoria_recetas != "Todas":
        recetas_mostrar = [r for r in recetas_mostrar if r['categoria'] == categoria_recetas.lower()[:-1]]
    for receta in recetas_mostrar:
        with st.expander(f"{receta['nombre']} | {receta['tiempo_preparacion']} | {receta['dificultad']}"):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write("**Ingredientes:**")
                for ing, datos in receta['ingredientes'].items():
                    st.write(f"- {ing.replace('_', ' ').title()}: {datos['cantidad']} {datos['unidad']}")
            with col2:
                st.write("**Preparacion:**")
                for i, paso in enumerate(receta['preparacion'], 1):
                    st.write(f"{i}. {paso}")
                st.write("**Informacion Nutricional:**")
                nutri = receta['informacion_nutricional']
                df_nutri = pd.DataFrame({
                    "Nutriente": ["Calorias", "Proteinas", "Carbohidratos", "Grasas", "Fibra"],
                    "Cantidad": [f"{nutri['calorias']} kcal", f"{nutri['proteinas']}g", f"{nutri['carbohidratos']}g", f"{nutri['grasas']}g", f"{nutri['fibra']}g"]
                })
                st.table(df_nutri)

# ========== TAB 5: CONGELAR Y PORCIONAR ==========
with tab5:
    st.header("🧊 Guía de Porcionado para Congelador")
    st.write("Divide las proteínas en bolsas etiquetadas con el día y comida. Así solo sacas lo que necesitas cada día.")

    PROTEINAS = ['gallina', 'pechuga_pollo', 'carne_mechar', 'bistec_res', 'filete_pescado',
                 'carne_molida', 'chicharron', 'jamon', 'atun', 'huevo', 'salchichas']

    proteinas_por_dia = {}
    for dia in st.session_state.menu:
        for comida in ['desayuno', 'almuerzo', 'cena']:
            receta = dia[comida]
            for ing, datos in receta['ingredientes'].items():
                if ing in PROTEINAS:
                    if ing not in proteinas_por_dia:
                        proteinas_por_dia[ing] = []
                    proteinas_por_dia[ing].append({
                        'dia': dia['dia'],
                        'comida': comida,
                        'cantidad': datos['cantidad'],
                        'unidad': datos['unidad'],
                        'receta': receta['nombre']
                    })

    if not proteinas_por_dia:
        st.info("No se encontraron proteínas en el menú actual.")
    else:
        for proteina, usos in proteinas_por_dia.items():
            with st.expander(f"🍖 {proteina.replace('_', ' ').title()} ({len(usos)} usos)"):
                for u in sorted(usos, key=lambda x: x['dia']):
                    st.write(f"**Día {u['dia']} - {u['comida'].title()}**: {u['cantidad']} {u['unidad']} → {u['receta']}")
                total = sum(u['cantidad'] for u in usos)
                st.write(f"**Total a comprar:** {total} {usos[0]['unidad']}")
                st.write("---")
                st.caption("💡 Consejo: Pesa cada porción en bolsas separadas, etiqueta con día y comida, y congela plano.")

st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: gray;'>"
    f"<p>🥗 Planificador de Comidas Saludable | Hecho con ❤️ para {PERSONA1} y {PERSONA2}</p>"
    f"<p>Recetas colombo-venezolanas | Porciones para 2 personas | Plan de {DIAS_PLAN} dias</p>"
    f"</div>",
    unsafe_allow_html=True
)