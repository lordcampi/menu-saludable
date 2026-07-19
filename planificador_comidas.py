import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

from data.menu_generator import MenuGenerator
from data.inventory import InventoryManager
from data.menu_fijo import DIAS_PLAN
from data.hogar import (
    cargar_miembros,
    get_miembros_activos,
    get_factor_consumo_total,
    get_factor_escalado,
    get_nombres_activos,
    set_miembro_activo,
    FACTOR_BASE_REFERENCIA,
)
from utils.nutrition import NutritionCalculator
from utils.precios import GestorPrecios
from ui.theme import cargar_estilos, callout, encabezado_pagina, encabezado_seccion

# ── Configuración de página ────────────────────────────────────────────
st.set_page_config(
    page_title="Planificador de Comidas | Hogar",
    page_icon="🥗",
    layout="wide",
)
cargar_estilos()

# ── Cargar miembros del hogar ──────────────────────────────────────────
miembros = cargar_miembros()
activos = get_miembros_activos(miembros)
factor_total = get_factor_consumo_total(miembros)
factor_escalado = get_factor_escalado(miembros)
nombres_activos = get_nombres_activos(miembros)

# ── Calculadora nutricional para N miembros ─────────────────────────────
calc = NutritionCalculator(miembros)
metas = calc.get_metas_personalizadas()


def _etiqueta_fuente(fuente: str, supermercado: str | None) -> str:
    if fuente == "scrape" and supermercado:
        return f"🟢 {supermercado}"
    if fuente == "referencia" and supermercado:
        return f"🟡 {supermercado} (ref.)"
    if fuente == "respaldo":
        return "🟠 Respaldo"
    return "⚪ Sin dato"


def _unir_nombres(nombres):
    if not nombres:
        return "Hogar"
    if len(nombres) == 1:
        return nombres[0]
    return f"{', '.join(nombres[:-1])} y {nombres[-1]}"


def _mostrar_tarjeta_comida(etiqueta, receta):
    st.markdown(f"#### {etiqueta}")
    with st.expander(receta["nombre"], expanded=True):
        st.caption(
            f"{receta['tiempo_preparacion']} · "
            f"{receta['dificultad'].capitalize()}"
        )
        nutri = receta["informacion_nutricional"]
        col_a, col_b = st.columns(2)
        col_a.metric("Calorías", f"{nutri['calorias']} kcal")
        col_b.metric("Proteínas", f"{nutri['proteinas']} g")
        col_a.metric("Carbohidratos", f"{nutri['carbohidratos']} g")
        col_b.metric("Grasas", f"{nutri['grasas']} g")

        st.markdown("**Ingredientes**")
        for ingrediente, datos in receta["ingredientes"].items():
            st.write(
                f"{ingrediente.replace('_', ' ').title()} · "
                f"{datos['cantidad']} {datos['unidad']}"
            )

        st.markdown("**Preparación**")
        for indice, paso in enumerate(receta["preparacion"], 1):
            st.write(f"{indice}. {paso}")


def _mostrar_bloque_compras(titulo, lista_compras, gestor_precios, organizar_fn):
    compras_organizadas = organizar_fn(lista_compras)
    st.markdown(f"### {titulo}")
    if not compras_organizadas:
        st.success("Nada que comprar en este bloque.")
        return 0
    for categoria, productos in compras_organizadas.items():
        with st.expander(f"{categoria} ({len(productos)} productos)"):
            for producto, datos in productos.items():
                st.write(f"- {producto.replace('_', ' ').title()}: {datos['cantidad']} {datos['unidad']}")
    resultado = gestor_precios.calcular_costo_lista(lista_compras)
    st.metric(
        label="Presupuesto estimado",
        value=f"${resultado['total']:,.0f} COP",
    )
    with st.expander("Ver desglose por producto"):
        for categoria, productos in compras_organizadas.items():
            st.write(f"**{categoria}**")
            total_categoria = 0
            for producto in productos:
                if producto in resultado["desglose"]:
                    detalle = resultado["desglose"][producto]
                    precio = detalle["costo"]
                    total_categoria += precio
                    etiqueta = _etiqueta_fuente(
                        detalle.get("fuente", "respaldo"),
                        detalle.get("supermercado"),
                    )
                    st.write(
                        f"- {producto.replace('_', ' ').title()}: "
                        f"${precio:,.0f} — {etiqueta}"
                    )
            st.caption(f"Subtotal · ${total_categoria:,.0f}")
    return resultado["total"]


def _inicializar_sesion():
    """Inicializa o reinicia el estado de sesión de Streamlit."""
    if "menu" not in st.session_state or st.session_state.get("_needs_reload", False):
        mg = MenuGenerator(dias=DIAS_PLAN)
        st.session_state.menu = mg.cargar_menu_fijo()
        st.session_state.menu_generator = mg
        st.session_state.inventory_manager = InventoryManager(st.session_state.menu)
        st.session_state["_needs_reload"] = False
    if "gestor_precios" not in st.session_state:
        st.session_state.gestor_precios = GestorPrecios()


_inicializar_sesion()

# ── Sidebar ────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## NutriPlan")
    st.caption("Planificación inteligente para el hogar")

    # ── Miembros del hogar ─────────────────────────────────────────────
    st.markdown("### Hogar")
    for miembro in miembros:
        estado = "Activo" if miembro["activo"] else "Inactivo"
        st.write(f"**{miembro['nombre']}** · {estado}")
        if miembro["activo"]:
            st.caption(
                f"{miembro['altura']} m · {miembro['peso']} kg · "
                f"Factor {miembro['factor_consumo']}"
            )
            if miembro["id"] in metas:
                meta = metas[miembro["id"]]
                objetivo = meta.get("objetivo", "mantener")
                if objetivo == "bajar_peso":
                    st.caption(f"  Meta: {meta['calorias_mantencion']} kcal/día (bajar a {meta['peso_objetivo']} kg)")
                else:
                    st.caption(f"  Meta: {meta['calorias_mantencion']} kcal/día")

    # ── Miembros opcionales ────────────────────────────────────────────
    st.markdown("### Configuración")
    miembros_por_id = {miembro["id"]: miembro for miembro in miembros}
    for miembro_id in ("carlos", "nilsa"):
        miembro = miembros_por_id[miembro_id]
        estado_actual = miembro["activo"]
        nuevo_estado = st.checkbox(
            f"Incluir a {miembro['nombre']} (factor {miembro['factor_consumo']:.2f})",
            value=estado_actual,
            key=f"activar_{miembro_id}",
            help=(
                f"Activa o desactiva a {miembro['nombre']}. "
                "El menú, inventario y compras se recalculan automáticamente."
            ),
        )
        if nuevo_estado != estado_actual:
            if set_miembro_activo(miembro_id, nuevo_estado):
                st.session_state["_needs_reload"] = True
                st.rerun()
            else:
                st.error(f"No se pudo guardar el estado de {miembro['nombre']}.")

    # ── Resumen del plan ───────────────────────────────────────────────
    st.markdown("### Resumen")
    st.caption(f"{DIAS_PLAN} días · Cocina colombo-venezolana")
    st.metric("Consumo del hogar", f"{factor_total:.2f}")
    if factor_total != FACTOR_BASE_REFERENCIA:
        delta = ((factor_total - FACTOR_BASE_REFERENCIA) / FACTOR_BASE_REFERENCIA) * 100
        st.caption(f"Escalado {delta:+.0f}% frente a la base")
    else:
        st.caption("Escalado 1.0× · Base")

# ── Título principal ────────────────────────────────────────────────────
nombres_str = _unir_nombres(nombres_activos)
encabezado_pagina(
    f"Plan nutricional · {DIAS_PLAN} días",
    "Comer bien, sin improvisar.",
    f"Menú, compras y porciones organizadas para {nombres_str}.",
    [
        f"{len(activos)} personas activas",
        f"Factor {factor_total:.2f}",
        "Cocina colombo-venezolana",
    ],
)

# ── Tabs ────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Menú diario",
        "Inventario y compras",
        "Análisis nutricional",
        "Recetario",
        "Congelar y porcionar",
    ]
)

# ═══════════════════════════════════════════════════════════════════════
# TAB 1: Menú Diario
# ═══════════════════════════════════════════════════════════════════════
with tab1:
    encabezado_seccion(
        "Plan de comidas",
        "Explora el detalle de cada comida y el balance nutricional del día.",
    )

    dia_seleccionado = st.selectbox(
        "Día del plan",
        range(1, DIAS_PLAN + 1),
        format_func=lambda x: f"Día {x}",
    )

    dia_menu = st.session_state.menu[dia_seleccionado - 1]

    col1, col2, col3 = st.columns(3)
    with col1:
        _mostrar_tarjeta_comida("Desayuno", dia_menu["desayuno"])

    with col2:
        _mostrar_tarjeta_comida("Almuerzo", dia_menu["almuerzo"])

    with col3:
        _mostrar_tarjeta_comida("Cena", dia_menu["cena"])

    st.markdown("### Balance del día")
    resumen = dia_menu["resumen_nutricional"]

    # Mostrar métricas para cada miembro activo
    cols_resumen = st.columns(3)
    cols_resumen[0].metric("Calorías totales", f"{resumen['calorias_totales']} kcal")
    cols_resumen[1].metric("Proteínas totales", f"{resumen['proteinas_totales']} g")
    cols_resumen[2].metric("Carbohidratos", f"{resumen['carbohidratos_totales']}g")

    if activos:
        st.caption("Metas individuales")
        cols_metas = st.columns(len(activos))
    for idx, miembro in enumerate(activos):
        miembro_id = miembro["id"]
        if miembro_id in metas:
            meta_kcal = metas[miembro_id]["calorias_mantencion"]
            pct = (resumen["calorias_totales"] / meta_kcal) * 100 if meta_kcal > 0 else 0
            cols_metas[idx].metric(
                f"% Meta {miembro['nombre']}",
                f"{pct:.0f}%",
            )

# ═══════════════════════════════════════════════════════════════════════
# TAB 2: Inventario y Compras
# ═══════════════════════════════════════════════════════════════════════
with tab2:
    encabezado_seccion(
        "Inventario y compras",
        "Registra tus existencias y organiza el mercado por frecuencia de compra.",
    )
    col1, col2 = st.columns([5, 7])
    with col1:
        st.subheader("Inventario actual")
        with st.form("inventario_form"):
            st.caption("Ingresa las cantidades disponibles en casa.")
            inventario_actual = {}
            for categoria, productos in st.session_state.inventory_manager.get_productos_para_formulario().items():
                st.write(f"**{categoria}**")
                for producto in productos:
                    datos = st.session_state.inventory_manager.inventario_necesario[producto]
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        st.caption(
                            f"{producto.replace('_', ' ').title()} "
                            f"(Necesario: {datos['cantidad']} {datos['unidad']})"
                        )
                    with col_b:
                        valor_guardado = st.session_state.inventory_manager.inventario_actual.get(
                            producto, 0.0
                        )
                        inventario_actual[producto] = st.number_input(
                            "Tengo",
                            min_value=0.0,
                            value=float(valor_guardado),
                            step=0.1,
                            key=f"inv_{producto}",
                            label_visibility="collapsed",
                        )
            if st.form_submit_button("Guardar inventario", width="stretch"):
                guardado = (
                    st.session_state.inventory_manager
                    .actualizar_inventario_actual(inventario_actual)
                )
                if guardado:
                    st.success("Inventario guardado.")
                    st.rerun()
                else:
                    st.error("No se pudo guardar el inventario. Revisa el acceso a la carpeta data.")

    with col2:
        st.subheader("Lista de mercado")
        ciudad = st.selectbox(
            "Ciudad",
            ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira"],
        )
        if st.session_state.inventory_manager.inventario_actual:
            inv_mgr = st.session_state.inventory_manager

            lista_quincenal = inv_mgr.generar_lista_compras_quincenal()
            listas_semanales = inv_mgr.generar_listas_compras_semanales()
            lista_completa = {**lista_quincenal}
            for bloque in listas_semanales.values():
                for producto, datos in bloque.items():
                    if producto in lista_completa:
                        lista_completa[producto] = {
                            "cantidad": lista_completa[producto]["cantidad"] + datos["cantidad"],
                            "unidad": datos["unidad"],
                            "tipo": datos["tipo"],
                        }
                    else:
                        lista_completa[producto] = datos

            gestor_precios = st.session_state.gestor_precios
            gestor_precios.ajustar_precios_por_ciudad(ciudad)

            col_btn, col_info = st.columns([1, 2])
            with col_btn:
                actualizar = st.button(
                    "Actualizar precios",
                    width="stretch",
                    help="Consulta precios en supermercados para los productos de tu lista",
                )
            with col_info:
                if gestor_precios.fecha_consulta:
                    fecha_txt = datetime.fromisoformat(
                        gestor_precios.fecha_consulta
                    ).strftime("%d/%m/%Y %H:%M")
                    st.caption(f"Última consulta: {fecha_txt}")
                else:
                    st.caption("Sin consulta reciente — usa precios de respaldo")

            if actualizar:
                progress = st.progress(0, text="Consultando supermercados...")
                productos_lista = list(lista_completa.keys())
                total_prod = max(len(productos_lista), 1)

                def on_progress(producto):
                    idx = productos_lista.index(producto) + 1 if producto in productos_lista else 0
                    progress.progress(
                        min(idx / total_prod, 1.0),
                        text=f"Buscando {producto.replace('_', ' ')}...",
                    )

                gestor_precios.obtener_precios(
                    lista_completa,
                    ciudad,
                    forzar_actualizacion=True,
                    on_progress=on_progress,
                )
                progress.progress(1.0, text="Precios actualizados")
                st.success("Precios actualizados para hoy")
            else:
                gestor_precios.preparar_precios(lista_completa, ciudad)

            resumen = gestor_precios.resumen_fuentes(lista_completa)
            if resumen["precios_respaldo"] > 0:
                st.warning(
                    f"{resumen['precios_respaldo']} producto(s) usan precio de respaldo. "
                    "Pulsa «Actualizar precios hoy» para intentar precios en vivo."
                )
            if resumen["supermercados"]:
                st.caption(
                    f"Fuentes: {', '.join(resumen['supermercados'])} | "
                    f"{resumen['precios_vivos']}/{resumen['total_productos']} con precio consultado"
                )

            st.caption(
                "Compra frutas, verduras, tubérculos, lácteos y embutidos cada semana; "
                "los congelables y productos de despensa se compran para los 15 días."
            )

            total_quincenal = _mostrar_bloque_compras(
                "Compra quincenal (15 días — sin perecederos)",
                lista_quincenal,
                gestor_precios,
                inv_mgr.organizar_por_categorias,
            )

            total_sem1 = _mostrar_bloque_compras(
                "Compra semanal — Semana 1 (días 1–7, perecederos)",
                listas_semanales["semana_1"],
                gestor_precios,
                inv_mgr.organizar_perecederos,
            )

            total_sem2 = _mostrar_bloque_compras(
                "Compra semanal — Semana 2 (días 8–15, perecederos)",
                listas_semanales["semana_2"],
                gestor_precios,
                inv_mgr.organizar_perecederos,
            )

            if total_quincenal or total_sem1 or total_sem2:
                st.metric(
                    label="Total estimado (quincenal + 2 semanas)",
                    value=f"${total_quincenal + total_sem1 + total_sem2:,.0f} COP",
                    delta=f"Precios {ciudad}",
                )
        else:
            st.info("Guarda tu inventario para generar la lista de compras.")

# ═══════════════════════════════════════════════════════════════════════
# TAB 3: Análisis Nutricional
# ═══════════════════════════════════════════════════════════════════════
with tab3:
    encabezado_seccion(
        "Análisis nutricional",
        "Compara la energía del menú con las metas activas del hogar.",
    )
    analisis = calc.analizar_menu(st.session_state.menu)

    col1, col2, col3 = st.columns(3)
    col1.metric("Calorías por día", f"{analisis['promedio_calorias']} kcal")
    col2.metric("Proteínas por día", f"{analisis['promedio_proteinas']} g")
    col3.metric("Días planificados", DIAS_PLAN)

    st.subheader("Evolución de calorías")
    calorias_por_dia = [
        dia["resumen_nutricional"]["calorias_totales"] for dia in st.session_state.menu
    ]
    df = pd.DataFrame({"Día": range(1, DIAS_PLAN + 1), "Calorías": calorias_por_dia})
    for miembro in activos:
        miembro_id = miembro["id"]
        if miembro_id in metas:
            df[f"Meta {miembro['nombre']}"] = [metas[miembro_id]["calorias_mantencion"]] * DIAS_PLAN
    fig = px.line(
        df,
        x="Día",
        y=[c for c in df.columns if c != "Día"],
        title="Calorías por día frente a metas",
        color_discrete_sequence=["#58D6A3", "#72A7FF", "#F3C969", "#C58AF9", "#FF8C8C"],
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#DDE8F0",
        legend_title_text="",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    fig.update_xaxes(gridcolor="rgba(151,175,194,0.10)")
    fig.update_yaxes(gridcolor="rgba(151,175,194,0.10)")
    st.plotly_chart(fig, width="stretch", theme=None)

    col1, col2 = st.columns(2)
    with col1:
        prom_desayuno = (
            sum(d["desayuno"]["informacion_nutricional"]["calorias"] for d in st.session_state.menu)
            / DIAS_PLAN
        )
        prom_almuerzo = (
            sum(d["almuerzo"]["informacion_nutricional"]["calorias"] for d in st.session_state.menu)
            / DIAS_PLAN
        )
        prom_cena = (
            sum(d["cena"]["informacion_nutricional"]["calorias"] for d in st.session_state.menu)
            / DIAS_PLAN
        )
        df_comidas = pd.DataFrame(
            {
                "Comida": ["Desayuno", "Almuerzo", "Cena"],
                "Calorias": [prom_desayuno, prom_almuerzo, prom_cena],
            }
        )
        fig2 = px.pie(
            df_comidas,
            values="Calorias",
            names="Comida",
            title="Distribución calórica",
            color_discrete_sequence=["#58D6A3", "#72A7FF", "#F3C969"],
            hole=0.62,
        )
        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#DDE8F0",
            legend_title_text="",
            margin=dict(l=10, r=10, t=60, b=10),
        )
        st.plotly_chart(fig2, width="stretch", theme=None)

    with col2:
        st.subheader("Recomendaciones")
        for rec in analisis["recomendaciones"]:
            st.write(rec)

        # Info de cada miembro activo
        info_lines = []
        for miembro in activos:
            miembro_id = miembro["id"]
            if miembro_id not in metas:
                continue
            meta = metas[miembro_id]
            objetivo = meta.get("objetivo", "mantener")
            if objetivo == "bajar_peso":
                info_lines.append(
                    f"**{miembro['nombre']}** ({meta['altura']} m, {meta['peso']} kg → "
                    f"{meta['peso_objetivo']} kg): bajar peso — {meta['calorias_mantencion']} kcal/día"
                )
            else:
                info_lines.append(
                    f"**{miembro['nombre']}** ({meta['altura']} m, {meta['peso']} kg): "
                    f"mantener peso — {meta['calorias_mantencion']} kcal/día"
                )

        info_lines.append("- Beber 2-3 litros de agua al día")
        info_lines.append("- Realizar 30 min de actividad física")
        info_lines.append("- Evitar azúcares refinados")
        st.info("\n".join(info_lines))

# ═══════════════════════════════════════════════════════════════════════
# TAB 4: Recetario
# ═══════════════════════════════════════════════════════════════════════
with tab4:
    encabezado_seccion(
        "Recetario",
        "Consulta ingredientes, preparación, nutrición y costo estimado.",
    )
    categoria_recetas = st.selectbox(
        "Categoría", ["Todas", "Desayunos", "Almuerzos", "Cenas"]
    )
    recetas_mostrar = st.session_state.menu_generator.get_todas_las_recetas()
    if categoria_recetas != "Todas":
        cat_map = {"Desayunos": "desayuno", "Almuerzos": "almuerzo", "Cenas": "cena"}
        recetas_mostrar = [
            r for r in recetas_mostrar if r["categoria"] == cat_map[categoria_recetas]
        ]

    gestor_recetas = st.session_state.gestor_precios
    if not gestor_recetas.precios:
        gestor_recetas.cargar_respaldo_completo()

    for receta in recetas_mostrar:
        costo_receta = gestor_recetas.calcular_costo_receta(receta["ingredientes"])
        with st.expander(
            f"{receta['nombre']} | {receta['tiempo_preparacion']} | "
            f"${costo_receta['total']:,.0f} COP"
        ):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write("**Ingredientes**")
                for ing, datos in receta["ingredientes"].items():
                    st.write(
                        f"- {ing.replace('_', ' ').title()}: "
                        f"{datos['cantidad']} {datos['unidad']}"
                    )
                st.metric(
                    f"Costo estimado · factor {factor_total:.1f}",
                    f"${costo_receta['total']:,.0f} COP",
                )
            with col2:
                st.write("**Preparación**")
                for i, paso in enumerate(receta["preparacion"], 1):
                    st.write(f"{i}. {paso}")
                st.write("**Información nutricional**")
                nutri = receta["informacion_nutricional"]
                df_nutri = pd.DataFrame(
                    {
                        "Nutriente": ["Calorías", "Proteínas", "Carbohidratos", "Grasas", "Fibra"],
                        "Cantidad": [
                            f"{nutri['calorias']} kcal",
                            f"{nutri['proteinas']}g",
                            f"{nutri['carbohidratos']}g",
                            f"{nutri['grasas']}g",
                            f"{nutri['fibra']}g",
                        ],
                    }
                )
                st.table(df_nutri)

# ═══════════════════════════════════════════════════════════════════════
# TAB 5: Congelar y Porcionar
# ═══════════════════════════════════════════════════════════════════════
with tab5:
    encabezado_seccion(
        "Congelar y porcionar",
        "Prepara porciones listas para cada día y evita desperdicios.",
    )
    callout(
        "Divide las carnes y pescados crudos en bolsas etiquetadas con el dia y comida. "
        "Mantén empanadas y carimañolas precongeladas separadas por uso. "
        "Jamón, huevo, atún en lata y embutidos se conservan según su empaque.",
        "Conservación",
    )

    porciones_congelacion = (
        st.session_state.inventory_manager.generar_porciones_congelacion()
    )

    if not porciones_congelacion:
        st.info("No se encontraron proteínas en el menú actual.")
    else:
        for proteina, grupo in porciones_congelacion.items():
            usos = grupo["usos"]
            with st.expander(
                f"{proteina.replace('_', ' ').title()} · {len(usos)} usos"
            ):
                for u in sorted(usos, key=lambda x: x["dia"]):
                    st.write(
                        f"**Día {u['dia']} · {u['comida'].title()}**: "
                        f"{u['cantidad']} {u['unidad']} → {u['receta']}"
                    )
                st.write(
                    f"**Total a porcionar:** {grupo['total_necesario']} "
                    f"{grupo['unidad']}"
                )
                st.write(
                    f"**Falta comprar:** {grupo['faltante_comprar']} "
                    f"{grupo['unidad']}"
                )
                st.caption(
                    "Pesa cada porción, etiqueta con día y comida, y congela en plano."
                )

# ── Footer ─────────────────────────────────────────────────────────────
st.markdown(
    f"<div class='app-footer'>"
    f"<strong>NutriPlan</strong> · Diseñado para {nombres_str}<br>"
    f"Recetas colombo-venezolanas · Factor {factor_total:.1f} · "
    f"Plan de {DIAS_PLAN} días"
    f"</div>",
    unsafe_allow_html=True,
)